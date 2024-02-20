from datetime import date
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QAbstractTableModel, Qt, QThread
from UIFiles.ui_specialAlerts import Ui_specialAlerts

from ProjectPages.searchDlg import SearchDlg
from ProjectPages.messageDlg import MessageDlg
from workers import SpecialAlertsWorker

import mysql.connector
from mysql.connector import errorcode
import pandas as pd


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
        self._data.reset_index(drop = True, inplace= True) #by defualt old index is added as column drop= True drops that added column of older index
        self.layoutChanged.emit()

    def clear(self):
        self.layoutAboutToBeChanged.emit()
        self._data = self._data[0:0]
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

class SpecialAlerts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_specialAlerts()
        self.ui.setupUi(self)
        self.setWindowTitle('Special Alerts')
        self.ui.tbvSpecialAlertsStkList.horizontalHeader().setStretchLastSection(True)
        self.ui.tbvSpecialAlertsStkList.horizontalHeader().setDefaultSectionSize(200)


        self.specialAlertsWorker = SpecialAlertsWorker()
        self.specialAlertThread = QThread()
        self.specialAlertsWorker.isSpecialAlertsPage = True
        self.specialAlertsWorker.moveToThread(self.specialAlertThread)

        self.specialAlertThread.started.connect(self.specialAlertsWorker.getAlertsTriggeredStkList)
        self.specialAlertsWorker.sigSpecialAlerts.connect(self.showSpecialAlertsTriggeredList)
        self.specialAlertsWorker.finished.connect(self.specialAlertThread.quit)
        self.specialAlertsWorker.finished.connect(self.specialAlertThread.wait)
        self.specialAlertsWorker.finished.connect(self.specialAlertsWorker.deleteLater)
        self.specialAlertsWorker.finished.connect(self.specialAlertThread.deleteLater)
        self.specialAlertThread.start()

        self.addConnectors()
        self.showSpecialAlertsStkList()

    def addConnectors(self):
        self.ui.btnAdd.clicked.connect(self.showSearchDlg)
        self.ui.btnDelete.clicked.connect(self.deleteFromStkList)
        self.ui.btnImport.clicked.connect(self.importStocksList)
        self.ui.btnClearAll.clicked.connect(self.deleteAllFromStkList)
        self.ui.btnDownload.clicked.connect(self.downloadSpecialAlertsTriggeredList)

    def getSpecialAlertsStkList(self):
        stkList = {'stkSymbol': [], 'stkName' : []}
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select stkSymbol, stkName from special_alerts_stk_list"""
            cursor.execute(query)
            for (stkSymbol, stkName) in cursor:
                stkList["stkSymbol"].append(stkSymbol) 
                stkList["stkName"].append(stkName)          

            return pd.DataFrame(stkList, columns=stkList.keys())
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            cursor.close()
            con.close()

    def showSpecialAlertsStkList(self): 
        wlData = self.getSpecialAlertsStkList()
        self.model = TableModel(wlData)
        self.ui.tbvSpecialAlertsStkList.setModel(self.model)

    def showSearchDlg(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.addToSpecialAlertsStkList)
        self.dlgSearch.show()

    def addToSpecialAlertsStkList(self):
        modelIndexls = self.dlgSearch.ui.tblvSuggestions.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()
            query = f"""insert into special_alerts_stk_list(stkSymbol, stkName) values('{stkSym}', '{stkName}')"""
            print(query)
            cursor.execute(query)
            con.commit()

            self.model.addRow(pd.DataFrame({'stkSymbol': [stkSym], 'stkName': [stkName]}, columns=['stkSymbol', 'stkName']))
            print(stkName, 'added to special_alerts_stk_list')
            
            self.specialAlertsWorker.addToSymbolsList(stkSym) #add stock in list of worker
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()
    
    def importStocksList(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'import file', 'C:\Downloads', 'Excel Files (*.csv)')
        df = pd.read_csv(filePath)
        df.columns = ['stkSymbol', 'stkName']
        # print(df.head(5))

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            for index, row in df.iterrows():
                query = f"""insert into special_alerts_stk_list(stkSymbol, stkName) values('{row['stkSymbol']}', '{row['stkName']}')"""
                cursor.execute(query)
                con.commit()

                self.specialAlertsWorker.addToSymbolsList(row['stkSymbol']) #add stock in a list of worker

            self.model.addRow(df)

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

    def deleteFromStkList(self):
        modelIndexls = self.ui.tbvSpecialAlertsStkList.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        
        if(len(modelIndexls) == 0):
            return

        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)
        rowIndex = self.ui.tbvSpecialAlertsStkList.currentIndex().row()

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()
            query = f"""delete from special_alerts_stk_list where stkSymbol = '{stkSym}'"""
            cursor.execute(query)
            con.commit()

            self.model.delRow(rowIndex)
            print(stkName, 'deleted from special_alerts_stk_list')

            self.specialAlertsWorker.deleteFromSymbolsList(stkSym) #delete stock from a list of worker

            self.ui.tbvSpecialAlertsStkList.clearSelection()
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

    def deleteAllFromStkList(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()
            query = f"""delete from special_alerts_stk_list"""
            cursor.execute(query)
            con.commit()

            self.model.clear() #clear data from tabel
            print('cleared all from special_alerts_stk_list')

            self.specialAlertsWorker.clearSymbolsList() #clear the list of symbols in the specialAlertsWorker
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

    def showSpecialAlertsTriggeredList(self, list):
        model = TableModel(list)
        self.ui.tbvTodaysTriggered.setModel(model)

        if(len(list.index) != 1):
            self.ui.lblNotification.setText(str(len(list.index)) + ' stocks have triggered the special alerts condition')
        else:
            self.ui.lblNotification.setText('1 stock has triggered the special alerts condition')

    def showMessage(self, msg):
        self.msgDlg = MessageDlg(msg)
        self.msgDlg.show()

    def downloadSpecialAlertsTriggeredList(self):
        stkList = self.ui.tbvTodaysTriggered.model()._data['stkSymbol']
        stkList.to_csv (r'C:\Downloads\stkList'+ date.today().strftime('%d-%m-%Y') +'.csv', index = None, encoding='utf-8', header=True)
        self.showMessage('list downloaded successfully')

    def closeEvent(self, event):
        print('closing stockDetails Window')
        self.specialAlertsWorker.isSpecialAlertsPage = False
        event.accept()
        print('closed stockDetails Window')

