from PySide6.QtCore import QAbstractTableModel, Qt, QThread
from PySide6.QtWidgets import QMainWindow, QHeaderView
from ProjectPages.watchlistDetailsDlg import WatchlistDetailsDlg
from ProjectPages.searchDlg import SearchDlg
from UIFiles.ui_watchlists import Ui_watchlists
from workers import WatchlistWorker

import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import yfinance as yf

# TODOO: add synchronization to self.watchlistData because when we change the watchlist watchlist data changes

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

        self.watchlistWorker = WatchlistWorker()
        self.watchlistThread = QThread()
        self.watchlistWorker.moveToThread(self.watchlistThread)

        self.watchlistWorker.isRunning = True
        self.watchlistWorker.watchlistData = self.watchlistData
        self.watchlistThread.started.connect(self.watchlistWorker.getWatchlistTableModel)
        self.watchlistWorker.sigChngWLData.connect(self.changeWLData)

        self.addConnectors()
        self.loadWatchlists()

        count = self.ui.cmbWatchlists.count()
        if count != 0: #if there are 1 or more watchlist show the data of 1st
            WLName = self.ui.cmbWatchlists.currentText()
            self.showWatchlistData(WLName)
        else: #no watchlist is created
            self.ui.cmbWatchlists.hide()
            self.ui.frmWLContent.hide()
        
        self.manageVisibility()
        self.watchlistThread.start() #a lot to work on this
    
    def addConnectors(self):
        self.ui.btnCreateWL.clicked.connect(self.getWatchlistDetails)
        self.ui.btnAddToWL.clicked.connect(self.showSearchDlg)
        self.ui.btnDeleteFrmWL.clicked.connect(self.deleteStockFrmWL)

        self.ui.cmbWatchlists.currentTextChanged.connect(self.watchlistWorker.setWatchlistChanged)
        self.ui.cmbWatchlists.currentTextChanged.connect(lambda: self.showWatchlistData(self.ui.cmbWatchlists.currentText()))
        

    def loadWatchlists(self):
        count = 0
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
            cursor = con.cursor()
            query = f"""show tables;"""
            cursor.execute(query)
            for tableName, in cursor:
                self.ui.cmbWatchlists.addItem(tableName)
                count += 1

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close() 
        
    def showWatchlistData(self, watchlist): 
        stkSymbols = []
        stkNames = []
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

            self.watchlistData = data
            # print(self.watchlistData.head())
            model = TableModel(self.watchlistData)
            self.ui.tbvWatchlist.setModel(model)

        else:
            self.watchlistData = pd.DataFrame({})
        
        self.watchlistWorker.watchlistData = self.watchlistData
        self.manageVisibility()
        
    def getWatchlistDetails(self):

        #get watchlist details
        self.watchlistDetails = WatchlistDetailsDlg()
        self.watchlistDetails.ui.btnCreate.clicked.connect(self.createWatchlistInDB)
        self.watchlistDetails.ui.btnCreate.clicked.connect(lambda: self.watchlistDetails.close()) #close the watchlistDetails dialog

        self.watchlistDetails.show()
    
    def createWatchlistInDB(self):
        name = self.watchlistDetails.ui.leName.text()
        # TODOO : you can create single table in Db and just add the extra column of watchlistName
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
            cursor = con.cursor()
            query = f"""create table {name} (stkSymbol varchar(25) primary key, stkName varchar(75))"""
            print(query)
            cursor.execute(query)
            con.commit()

            #display stocks in the watchlist 
            self.showWatchlistData(name)
            self.ui.cmbWatchlists.addItem(name)
            self.ui.cmbWatchlists.setCurrentText(name)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()
        
        # self.watchlistDetails.close() #close the watchlistDetails dialog

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

            #change data in worker to get live updates
            self.watchlistWorker.watchlistData = self.watchlistData
            
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
        
        self.manageVisibility()

    def showSearchDlg(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.addToWatchlist)
        self.dlgSearch.show()

    def deleteStockFrmWL(self):
        modelIndexls = self.ui.tbvWatchlist.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)
        
        #delete from database
        tblName = self.ui.cmbWatchlists.currentText()
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='watchlists_db')
            cursor = con.cursor()
            query = f"""delete from {tblName} where stkSymbol = '{stkSym}'"""
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

        index = self.watchlistData.index[self.watchlistData['Symbol'] == stkSym]
        self.watchlistData.drop(index, axis= 0, inplace= True)
        self.watchlistWorker.watchlistData.drop(index, axis= 0, inplace= True) #delete from worker's watchlist data

        if self.watchlistData.size != 0:
            model = TableModel(self.watchlistData)
            self.ui.tbvWatchlist.setModel(model)

        self.manageVisibility()
    
    def manageVisibility(self): #manages the visibility of watchlist table and msg label
        if self.watchlistData.size != 0:
            self.ui.lblMsg.hide()
            self.ui.tbvWatchlist.setVisible(True)
        else:
            self.ui.tbvWatchlist.hide()
            self.ui.lblMsg.setVisible(True)
    
    def changeWLData(self, data):
        model = TableModel(pd.DataFrame(data, columns=['Symbol', 'Name', 'Open', 'High', 'Low', 'Close']))
        self.ui.tbvWatchlist.setModel(model)
    
    def closeEvent(self, event):
        print('closing watchlist window')
        self.watchlistWorker.isRunning = False
        self.watchlistThread.quit()
        self.watchlistThread.wait()
        event.accept()
        print('called closeWindow')