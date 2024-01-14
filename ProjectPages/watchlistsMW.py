from PySide6.QtCore import QAbstractTableModel, Qt, QThread, QReadWriteLock
from PySide6.QtWidgets import QMainWindow, QHeaderView, QFileDialog
from ProjectPages.watchlistDetailsDlg import WatchlistDetailsDlg
from ProjectPages.searchDlg import SearchDlg
from UIFiles.ui_watchlists import Ui_watchlists
from workers import WatchlistWorker
from APIMethods import getQuoteFromYfinance

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
    
    def delRow(self, index):
        self.layoutAboutToBeChanged.emit()
        self._data.drop(index, axis = 0, inplace = True)
        self.layoutChanged.emit()

    def addRow(self, row):
        self.layoutAboutToBeChanged.emit()
        self._data = pd.concat([self._data, row], ignore_index= True)
        self.layoutChanged.emit()

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

        self.watchlistWorker = WatchlistWorker()
        self.watchlistThread = QThread()
        self.watchlistWorker.moveToThread(self.watchlistThread)

        self.addConnectors()
        self.loadWatchlists()

        count = self.ui.cmbWatchlists.count()
        if count != 0: #if there are 1 or more watchlist show the data of 1st watchlist
            WLName = self.ui.cmbWatchlists.currentText()
            self.watchlistWorker.currWL = WLName
            self.watchlistWorker.getWLSymbols(WLName) 
        
        self.manageVisibility()

        self.watchlistThread.started.connect(self.watchlistWorker.updateWL)   
        self.watchlistWorker.sigShowWLData.connect(self.showWatchlistData)
        '''the below thread.quit() and thread.wait() needs to be called to properly quit the thread'''
        self.watchlistWorker.finished.connect(self.watchlistThread.quit) 
        self.watchlistWorker.finished.connect(self.watchlistThread.wait)
        self.watchlistWorker.finished.connect(self.watchlistWorker.deleteLater)
        self.watchlistThread.finished.connect(self.watchlistThread.deleteLater)
        self.watchlistThread.start()

    
    def addConnectors(self):
        self.ui.btnCreateWL.clicked.connect(self.getWatchlistDetails)
        self.ui.btnAddToWL.clicked.connect(self.showSearchDlg)
        self.ui.btnDeleteFrmWL.clicked.connect(self.deleteStockFrmWL)
        self.ui.btnImport.clicked.connect(self.importStocksList)

        self.ui.cmbWatchlists.currentTextChanged.connect(lambda : self.watchlistWorker.setWatchlistChanged(self.ui.cmbWatchlists.currentText()))        
        

    def loadWatchlists(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
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
        
    def showWatchlistData(self, wlData): 
        print(wlData)
        self.model = TableModel(wlData)
        self.ui.tbvWatchlist.setModel(self.model)
        
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
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
            cursor = con.cursor()
            query = f"""create table {name} (stkSymbol varchar(25) primary key, stkName varchar(75))"""
            print(query)
            cursor.execute(query)
            con.commit()

            #display stocks in the watchlist 
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
        
    
    def addToWatchlist(self):
        modelIndexls = self.dlgSearch.ui.tblvSuggestions.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)

        #insert data in database
        watchlist = self.ui.cmbWatchlists.currentText()
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
            cursor = con.cursor()
            query = f"""insert into {watchlist} values('{stkSym}', '{stkName}')"""
            print(query)
            cursor.execute(query)
            con.commit()

            self.watchlistWorker.stkList[stkSym] = stkName #add stock in worker list
            
            try:
                # currPrice = json.loads(getQuote2('shubh',alert['stkSymbol'], 'tc', 'NSE'))['data']['close']
                stk = getQuoteFromYfinance('shubh', stkSym, 'tc', 'NSE')
                self.model.addRow(pd.DataFrame( {'Symbol' : [stkSym], 
                                                 'Name' : [stkName], 
                                                 'Open' : [round(stk['Open'].item(), 2)], 
                                                 'High' : [round(stk['High'].item(), 2)], 
                                                 'Low' : [round(stk['Low'].item(), 2)], 
                                                 'Close' : [round(stk['Close'].item(), 2)]} ))     
            except Exception as e:
                print(e)

            print(stkName, 'added to watchlist', watchlist)
            
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
    
    def importStocksList(self):
        watchlist = self.ui.cmbWatchlists.currentText()
        filePath, _ = QFileDialog.getOpenFileName(self, 'import file', 'C:\Downloads', 'Excel Files (*.csv)')
        print(filePath)
        df = pd.read_csv(filePath)
        # print(df.head(5))

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
            cursor = con.cursor()

            for index, row in df.iterrows():
                query = f"""insert into {watchlist} values('{row['symbol']}', '{row['name']}')"""
                cursor.execute(query)
                con.commit()

                self.watchlistWorker.stkList[row['symbol']] = row['name'] #add stock in worker list


            print('data imported successfully')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        except Exception as e:
            print('exception in watchlistsMW', e)
        else:
            con.close()        

    def showSearchDlg(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.addToWatchlist)
        self.dlgSearch.show()

    def deleteStockFrmWL(self):
        modelIndexls = self.ui.tbvWatchlist.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)
        rowIndex = self.ui.tbvWatchlist.currentIndex().row()
        
        #delete from database
        watchlist = self.ui.cmbWatchlists.currentText()
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
            cursor = con.cursor()
            query = f"""delete from {watchlist} where stkSymbol = '{stkSym}'"""
            cursor.execute(query)
            con.commit()

            self.watchlistWorker.stkList.pop(stkSym) #delete from worker list
            self.model.delRow(rowIndex)
            print(stkName, 'deleted from watchlist', watchlist)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        except Exception as e: #If the key is not found in dict then dict.pop might raise a KeyError.
            print(e)
        else:
            con.close()
            
    
    def manageVisibility(self): #manages the visibility of watchlist table and msg label
        count = self.ui.cmbWatchlists.count()
        if count != 0: #if there is atleast 1 watchlist then show the watchlist frame and list of watchlists in combobox
            self.ui.cmbWatchlists.setVisible(True)
            self.ui.frmWLContent.setVisible(True)
        else: #no watchlist is created
            self.ui.cmbWatchlists.hide()
            self.ui.frmWLContent.hide()

        if len(self.watchlistWorker.stkList.keys()) != 0: #if atleast 1 stock in watchlist
            self.ui.lblMsg.hide()
            self.ui.tbvWatchlist.setVisible(True)
        else:
            self.ui.tbvWatchlist.hide()
            self.ui.lblMsg.setVisible(True)
        print('callled manageVisibility')
    
    
    #this function causing crash  to the system don't know why
    def closeEvent(self, event):
        print('closing watchlist window')
        
        self.watchlistWorker.isRunning = False
        print('called closeWindow')
        event.accept()

        
        