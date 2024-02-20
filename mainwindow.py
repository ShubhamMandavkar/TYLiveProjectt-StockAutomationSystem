# This Python file uses the following encoding: utf-8
import asyncio
import sys
from PySide6.QtCore import  QThread
from PySide6.QtWidgets import QApplication, QMainWindow
import requests

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py 

from UIFiles.ui_home import Ui_Home
from ProjectPages.searchDlg import SearchDlg
from ProjectPages.myAlertsMW import MyAlerts
from ProjectPages.specialAlertsMW import SpecialAlerts
from ProjectPages.holdingsMW import Holdings
from ProjectPages.watchlistsMW import Watchlists
from ProjectPages.customDetailsMW import CustomDetails
from ProjectPages.stockDetailsMW import StockDetails
from ProjectPages.messageDlg import MessageDlg
from ProjectPages.buyOrderDlg import BuyOrderDlg
from ProjectPages.sellOrderDlg import SellOrderDlg
from ProjectPages.myOrdersMW import MyOrders
from workers import AlertWorker, HoldingsWorker, SpecialAlertsWorker, TeleApiWorker

import mysql.connector
from mysql.connector import errorcode

#TODOO: need to resolve holding crash issue when 2 holdings window created app crashes

class UserDetails:
    def __init__(self):
        self.apiKey = ''
        self.apiSecretKey = ''
        self.profitThreshold = 100000
    
    def getUserDetails(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select apiKey, apiSecretKey, profitThreshold from customer_details where userId = '{'shubh'}'"""
            cursor.execute(query)
            for (key, sKey, profitThld) in cursor:
                self.apiKey = key
                self.apiSecretKey = sKey 
                self.profitThreshold = profitThld           

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

class Navigation: 
    holdings = [] #it is used to store multiple instances of stkDetails pages if single variable used and we attept to open another instance then program crashes due to thread running in background
    stkDetails  = [] #it is used to store multiple instances of stkDetails pages if single variable used and we attept to open another instance then program crashes due to thread running in background
    def showSearchDialog(self):
        self.dlgSearch = SearchDlg()
        self.dlgSearch.show()
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.showStkDetails)
        self.dlgSearch.ui.tblvSuggestions.doubleClicked.connect(self.dlgSearch.close)

    def showStkDetails(self):
        modelIndexls = self.dlgSearch.ui.tblvSuggestions.selectedIndexes() #return list of QModelIndices i.e. columns in a row
        stkSym = modelIndexls[0].data(0)
        stkName = modelIndexls[1].data(0)

        try:
            self.stkDetails.append(StockDetails(stkSym, stkName)) 
            self.stkDetails[-1].show()
        except requests.exceptions.ConnectionError as e:
            dlg = MessageDlg('Please check your internet connection')
            dlg.show()
            print('Please check your internet connection')
        except Exception as e:
            print('Exception occur in stockDetails.py', e)
      
    def showMyAlertsWindow(self):
        self.myAlerts = MyAlerts()
        self.myAlerts.show()

    def showSpecialAlertsWindow(self):
        self.specialAlerts = SpecialAlerts()
        self.specialAlerts.show()

    def showMyOrdersWindow(self):
        self.myOrders = MyOrders()
        # self.myOrders.show() # show() method is called in the constructor

    def showHoldingsWindow(self):
        self.holdings.append(Holdings()) 
        self.holdings[-1].show()
    
    def showWatchlistsWindow(self):
        self.watchlists = Watchlists()
        self.watchlists.show()
      
    def showCustomDetailsWindow(self):
        self.customDetails = CustomDetails()
        self.customDetails.ui.btnSave.clicked.connect(chnageHoldingsFetchingWorkerDetails)
        self.customDetails.ui.btnSave.clicked.connect(chnageHoldingsProcessingWorkerDetails)
        self.customDetails.show()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.setWindowTitle('Dashboard')

        self.userDetails = UserDetails()
        self.userDetails.getUserDetails()

        #navigation class
        self.nav = Navigation()

        self.addConnectors()
    
    def addConnectors(self):
        #navigation code
        self.ui.btnSearch.clicked.connect(self.nav.showSearchDialog)
        self.ui.btnMyAlerts.clicked.connect(self.nav.showMyAlertsWindow)
        self.ui.btnSpecialAlerts.clicked.connect(self.nav.showSpecialAlertsWindow)
        self.ui.btnMyOrders.clicked.connect(self.nav.showMyOrdersWindow)
        self.ui.btnHoldings.clicked.connect(self.nav.showHoldingsWindow)
        self.ui.btnWatchlists.clicked.connect(self.nav.showWatchlistsWindow)
        self.ui.btnCustomDetails.clicked.connect(self.nav.showCustomDetailsWindow)

    '''method called when user clicks on buy button of notification sent on windows'''
    def showBuyOrderWidget(self, stkSymbol): 
        print('buyOrderWidget shown')
        self.orderWidget = BuyOrderDlg(stkSymbol)
        self.orderWidget.show()

    '''method called when user clicks on sell button of notification sent on windows'''
    def showSellOrderWidget(self): 
        self.orderWidget = SellOrderDlg()
        self.orderWidget.show()

    def showHoldingDetails(self, holdDetails):
        self.ui.lblTotalInvVal.setText(str(round(holdDetails['investedValue'].iloc[0], 2)))
        self.ui.lbalCurrentValueVal.setText(str(round(holdDetails['currentValue'].iloc[0], 2)))
        self.ui.lblPandLVal.setText(str(round(holdDetails['profitAndLoss'].iloc[0], 2)))

def chnageHoldingsFetchingWorkerDetails():
    widget.userDetails.getUserDetails()
    holdingsFetchingWorker.changeDetails(widget.userDetails.apiKey, widget.userDetails.apiSecretKey) 

def chnageHoldingsProcessingWorkerDetails():
    widget.userDetails.getUserDetails()
    holdingsProcessWorker.changeDetails(profitTh= widget.userDetails.profitThreshold) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    alertWorker = AlertWorker()
    alertThread = QThread()
    alertWorker.moveToThread(alertThread)
    alertWorker.isRunning = True 

    alertThread.started.connect(AlertWorker.getAlertList)
    alertThread.started.connect(alertWorker.processAlerts)
    alertWorker.sigShowBuyOrderWidget.connect(widget.showBuyOrderWidget)
    alertWorker.sigShowSellOrderWidget.connect(widget.showSellOrderWidget)

    #worker to fetch holdings details
    holdingsFetchingWorker = HoldingsWorker(widget.userDetails.apiKey, widget.userDetails.apiSecretKey)

    #Thread to fetch holdings continuously
    holdingsFetchingThread = QThread()
    holdingsFetchingWorker.moveToThread(holdingsFetchingThread)

    holdingsFetchingThread.started.connect(holdingsFetchingWorker.fetchHoldings)

    #worker to process holdings 
    holdingsProcessWorker = HoldingsWorker(profitTh= widget.userDetails.profitThreshold)
    holdingsProcessWorker.sigHoldDetails.connect(widget.showHoldingDetails)
    #Thread to process holdings
    holdingsProcessThread = QThread()
    holdingsProcessWorker.moveToThread(holdingsProcessThread)
    holdingsProcessThread.started.connect(holdingsProcessWorker.processHoldings)

    widget.show()
    holdingsFetchingThread.start()
    # holdingsProcessThread.start()

    loop = asyncio.new_event_loop() 
    teleApiWorker = TeleApiWorker(loop)
    teleApiThread = QThread() #this thread runs event loop required to send message on telegram
    teleApiWorker.moveToThread(teleApiThread)

    teleApiThread.started.connect(teleApiWorker.startEventLoop)
    teleApiWorker.finished.connect(teleApiThread.quit)
    teleApiWorker.finished.connect(teleApiWorker.deleteLater)
    teleApiThread.finished.connect(teleApiThread.deleteLater)
    teleApiThread.finished.connect(lambda: print('thread finished completely'))
    teleApiThread.start()
    
    # alertThread.start() #this thread should be started later than the teleApiThread

    specialAlertWorker = SpecialAlertsWorker()
    specialAlertThread = QThread()
    specialAlertWorker.moveToThread(specialAlertThread)

    specialAlertThread.started.connect(specialAlertWorker.getStkSymbolsList)
    specialAlertThread.started.connect(specialAlertWorker.check)
    specialAlertThread.start()

    sys.exit(app.exec())
