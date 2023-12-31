# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import  QThread
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QDialog
import requests

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py 


from UIFiles.ui_home import Ui_Home
from ProjectPages.searchDlg import SearchDlg
from ProjectPages.myAlertsMW import MyAlerts
from ProjectPages.holdingsMW import Holdings
from ProjectPages.watchlistsMW import Watchlists
from ProjectPages.customDetailsMW import CustomDetails
from ProjectPages.stockDetailsMW import StockDetails
from ProjectPages.messageDlg import MessageDlg
from workers import AlertWorker, HoldingsWorker

import mysql.connector
from mysql.connector import errorcode

class Navigation:
    def showSearchDialog(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.show()
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.showStkDetails)

    def showStkDetails(self):
        modelIndexls = self.dlgSearch.ui.tblvSuggestions.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)

        try:
            self.stkDetails = StockDetails(stkSym, stkName)
            self.stkDetails.show()
        except requests.exceptions.ConnectionError as e:
            dlg = MessageDlg('Please check your internet connection')
            dlg.show()
            print('Please check your internet connection')
        except Exception as e:
            print('Exception occur in stockDetails.py')

         
    def showMyAlertsWindow(self):
        self.myAlerts = MyAlerts()
        self.myAlerts.show()

    def showHoldingsWindow(self):
        self.holdings = Holdings()
        self.holdings.show()
    
    def showWatchlists(self):
        self.watchlists = Watchlists()
        self.watchlists.show()
        pass
      
    def showCustomDetails(self):
        self.customDetails = CustomDetails()
        self.customDetails.show()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        #navigation class
        self.nav = Navigation()

        self.addConnectors()
        self.getUserDetails()
    
    def getUserDetails(self):
        self.apiKey = 'key'
        self.apiSecretKey = 'mykey'
        pass
        # try:
        #     con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
        #     cursor = con.cursor()

        #     query = f"""select apiKey, apiSecretKey from customer_details where userId = '{'shubh'}'"""
        #     cursor.execute(query)
        #     for (key, sKey) in cursor:
        #         self.apiKey = key
        #         self.apiSecretKey = sKey            

        # except mysql.connector.Error as err:
        #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #         print("Something is wrong with your user name or password")
        #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #         print("Database does not exist")
        #     else:
        #         print("error:",err)
        # finally:
        #     cursor.close()
        #     con.close()

    def addConnectors(self):
        #navigation code
        self.ui.btnSearch.clicked.connect(self.nav.showSearchDialog)
        self.ui.btnMyAlerts.clicked.connect(self.nav.showMyAlertsWindow)
        self.ui.btnHoldings.clicked.connect(self.nav.showHoldingsWindow)
        self.ui.btnWatchlists.clicked.connect(self.nav.showWatchlists)
        self.ui.btnCustomDetails.clicked.connect(self.nav.showCustomDetails)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    alertWorker = AlertWorker()
    alertThread = QThread()
    alertWorker.moveToThread(alertThread)
    alertWorker.isRunning = True 

    alertThread.started.connect(AlertWorker.getAlertList)
    alertThread.started.connect(alertWorker.processAlerts)

    #worker to fetch holdings details
    holdingsFetchingWorker = HoldingsWorker(widget.apiKey, widget.apiSecretKey)

    #Thread to fetch holdings continuously
    holdingsFetchingThread = QThread()
    holdingsFetchingWorker.moveToThread(holdingsFetchingThread)

    holdingsFetchingThread.started.connect(holdingsFetchingWorker.fetchHoldings)

    #worker to process holdings
    holdingsProcessWorker = HoldingsWorker(widget.apiKey, widget.apiSecretKey)
    #Thread to process holdings
    holdingsProcessThread = QThread()
    holdingsProcessWorker.moveToThread(holdingsProcessThread)
    holdingsProcessThread.started.connect(holdingsProcessWorker.processHoldings)

    widget.show()
    alertThread.start()
    # holdingsFetchingThread.start()
    # holdingsProcessThread.start()
    sys.exit(app.exec())
