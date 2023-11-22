from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QMainWindow, QHeaderView
from ProjectPages.watchlistDetailsDlg import WatchlistDetailsDlg
from ProjectPages.searchDlg import SearchDlg
from UIFiles.ui_watchlists import Ui_watchlists

import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import yfinance as yf


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        return None

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    #essential to overide for custom header
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def sort(self, Ncol, order):
        """Sort table by given column number."""
        self.layoutAboutToBeChanged.emit()
        cols = self._data.columns
        self._data = self._data.sort_values(cols[Ncol],
                                      ascending=order == Qt.AscendingOrder)
        self.layoutChanged.emit()


class Watchlists(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_watchlists()
        self.ui.setupUi(self)

        self.watchlistData = pd.DataFrame({})

        self.showWatchlists()
        self.addConnectors()
    
    def addConnectors(self):
        self.ui.btnCreateWL.clicked.connect(self.getWatchlistDetails)
        self.ui.btnAddToWL.clicked.connect(self.showSearchDlg)

    def showWatchlists(self):
        self.count = 0
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000")
            cursor = con.cursor()
            query = f"""select count(*) as count from information_schema.tables where table_schema = 'watchlists_db';"""
            print(query)
            cursor.execute(query)
            for cnt, in cursor:
                self.count = cnt
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()

        if self.count != 0:
            #show the list of tables in a combobox
            try:
                con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
                cursor = con.cursor()
                query = f"""show tables;"""
                cursor.execute(query)
                for tableName, in cursor:
                    self.ui.cmbWatchlists.addItem(tableName)

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print("error:",err)
            else:
                con.close()
            

            stkSymbols = []
            stkNames = []

            #get the list of stkSymbols in watchlist table
            watchlist = self.ui.cmbWatchlists.currentText()
            try:
                con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
                cursor = con.cursor()
                query = f"""select * from {watchlist}"""
                cursor.execute(query)

                for stkSym, stkName in cursor:
                    stkSymbols.append(stkSym)
                    stkNames.append(stkName)

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print("error:",err)
            else:
                con.close()

            if len(stkSymbols ) != 0:#there are 1 or more stocks in watchlist
                #fetch data to show in table
                data = []
                for i in range(len(stkSymbols)):
                    #importing data from yfinance
                    stk = yf.Ticker(stkSymbols[i]+".NS")
                    hist = stk.history(period = '1d', interval = '1d')

                    #item method is used to retrieve data only else it return data with index
                    open =  round(hist['Open'].item(), 2)
                    high =  round(hist['High'].item(), 2)
                    low =  round(hist['Low'].item(), 2)
                    close =  round(hist['Close'].item(), 2)
                    data.append([stkSymbols[i], stkNames[i], open, high, low, close])
                
                # print(data)
                data = pd.DataFrame(data)
                data.columns = ['Symbol', 'Name', 'Open', 'High', 'Low', 'Close']

                self.watchlistData = pd.concat([self.watchlistData, data], ignore_index=True)
                model = TableModel(self.watchlistData)
                self.ui.tbvWatchlist.setModel(model)
            else: #if no stocks in watchlist
                self.ui.tbvWatchlist.hide()
                self.ui.lblMsg.setVisible(True)
        else:
            self.ui.cmbWatchlists.hide()
            self.ui.frmWLContent.hide()
        


    def getWatchlistDetails(self):
        self.watchlistDetails = WatchlistDetailsDlg()
        self.watchlistDetails.ui.btnCreate.clicked.connect(self.createWatchlist)
        self.watchlistDetails.show()
    
    def createWatchlist(self):
        name = self.watchlistDetails.ui.leName.text()
        # TODOO:you can create single table in Db and just add the extra column of watchlistName
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
            cursor = con.cursor()
            query = f"""create table {name} (stkSymbol varchar(25) primary key, stkName varchar(75))"""
            print(query)
            cursor.execute(query)
            con.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()

        self.watchlistDetails.close()

        self.showWatchlists()

    def addToWatchlist(self):
        modelIndexls = self.dlgSearch.ui.tblvSuggestions.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)

        #insert data in database
        tblName = self.ui.cmbWatchlists.currentText()
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
            cursor = con.cursor()
            query = f"""insert into {tblName} values('{stkSym}', '{stkName}')"""
            print(query)
            cursor.execute(query)
            con.commit()

            #importing data from yfinance
            stk = yf.Ticker(stkSym+".NS")
            hist = stk.history(period = '1d', interval = '1d')
            #item method is used to retrieve data only else it return data with index
            open =  round(hist['Open'].item(), 2)
            high =  round(hist['High'].item(), 2)
            low =  round(hist['Low'].item(), 2)
            close =  round(hist['Close'].item(), 2)
            self.watchlistData = pd.concat([ self.watchlistData, pd.DataFrame([[stkSym,stkName,open,high,low, close]], columns = ['Symbol', 'Name', 'Open', 'High', 'Low', 'Close'])], ignore_index= True)
            
            model = TableModel(self.watchlistData)
            self.ui.tbvWatchlist.setModel(model)
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()

    def showSearchDlg(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.addToWatchlist)
        self.dlgSearch.show()

