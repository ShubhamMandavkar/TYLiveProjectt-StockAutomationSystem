# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import  QThread
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QDialog

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
from workers import AlertWorker, HoldingsWorker

import mysql.connector
from mysql.connector import errorcode

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        self.addConnectors()
        self.getUserDetails()
    
    def getUserDetails(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select apiKey, apiSecretKey from customer_details where userId = '{'shubh'}'"""
            cursor.execute(query)
            for (key, sKey) in cursor:
                self.apiKey = key
                self.apiSecretKey = sKey            

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

    def addConnectors(self):
        self.ui.btnSearch.clicked.connect(self.showSearchDialog)
        self.ui.btnMyAlerts.clicked.connect(self.showMyAlertsWindow)
        self.ui.btnHoldings.clicked.connect(self.showHoldingsWindow)
        self.ui.btnWatchlists.clicked.connect(self.showWatchlists)
        self.ui.btnCustomDetails.clicked.connect(self.showCustomDetails)

    def showSearchDialog(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.show()
    
    def showMyAlertsWindow(self):
        self.myAlerts = MyAlerts()
        self.myAlerts.show()
    
    def showHoldingsWindow(self):
        self.holdings = Holdings()
        self.holdings.show()
    
    def showWatchlists(self):
        self.watchlists = Watchlists()
        self.watchlists.show()
      
    def showCustomDetails(self):
        self.customDetails = CustomDetails()
        self.customDetails.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    alertWorker = AlertWorker()
    alertThread = QThread()
    alertWorker.moveToThread(alertThread)
    alertWorker.isRunning = True 

    alertThread.started.connect(AlertWorker.getAlertList)
    alertThread.started.connect(alertWorker.processAlerts)

    holdingsWorker = HoldingsWorker(widget.apiKey, widget.apiSecretKey)
    holdingsThread = QThread()
    holdingsWorker.moveToThread(holdingsThread)

    holdingsThread.started.connect(holdingsWorker.fetchHoldings)
    holdingsThread.started.connect(holdingsWorker.processHoldings)

    widget.show()
    alertThread.start()
    holdingsThread.start()
    sys.exit(app.exec())
