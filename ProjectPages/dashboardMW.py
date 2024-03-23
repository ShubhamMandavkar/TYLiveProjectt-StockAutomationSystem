from PySide6.QtWidgets import QMainWindow

import asyncio
from PySide6.QtCore import  QThread
from PySide6.QtWidgets import QMainWindow
import requests

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
from workers import AlertWorker, HoldingsWorker, MyOrdersWorker, SpecialAlertsWorker, TeleApiWorker

import mysql.connector
from mysql.connector import errorcode
from UIFiles.ui_dashboard import Ui_Dashboard

class UserDetails:
    def __init__(self, userName):
        self.userName = userName
        self.apiKey = ''
        self.apiSecretKey = ''
        self.brCode = 'tc'
        self.profitThreshold = 100000
        self.averageThreshold = 100000
        self.deskNoti = True
        self.teleNoti = True
    
    def getUserDetails(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select apiKey, apiSecretKey, brCode, profitThreshold, averageThreshold, deskNoti, teleNoti from customer_details where userId = '{self.userName}'"""
            cursor.execute(query)
            for (key, sKey, brCode, profitThld, averageThld, deskNoti, teleNoti) in cursor:
                self.apiKey = key
                self.apiSecretKey = sKey 
                self.brCode = brCode
                self.profitThreshold = profitThld   
                self.averageThreshold = averageThld  
                self.deskNoti = deskNoti      
                self.teleNoti = teleNoti

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

class Dashboard(QMainWindow):
    holdings = [] #it is used to store multiple instances of stkDetails pages if single variable used and we attept to open another instance then program crashes due to thread running in background
    stkDetails  = [] #it is used to store multiple instances of stkDetails pages if single variable used and we attept to open another instance then program crashes due to thread running in background
    myOrders  = [] #it is used to store multiple instances of stkDetails pages if single variable used and we attept to open another instance then program crashes due to thread running in background
    specialAlerts  = [] #it is used to store multiple instances of stkDetails pages if single variable used and we attept to open another instance then program crashes due to thread running in background


    def __init__(self, userName, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.setWindowTitle('Dashboard')

        self.userDetails = UserDetails(userName)
        self.userDetails.getUserDetails()

        self.addConnectors()
        self.startWorkers()
    
    def addConnectors(self):
        #navigation code
        self.ui.btnSearch.clicked.connect(self.showSearchDialog)
        self.ui.btnMyAlerts.clicked.connect(self.showMyAlertsWindow)
        self.ui.btnSpecialAlerts.clicked.connect(self.showSpecialAlertsWindow)
        self.ui.btnMyOrders.clicked.connect(self.showMyOrdersWindow)
        self.ui.btnHoldings.clicked.connect(self.showHoldingsWindow)
        self.ui.btnWatchlists.clicked.connect(self.showWatchlistsWindow)
        self.ui.btnCustomDetails.clicked.connect(self.showCustomDetailsWindow)

    def startWorkers(self):
        self.alertWorker = AlertWorker(self.userDetails.deskNoti, self.userDetails.teleNoti)
        self.alertThread = QThread()
        self.alertWorker.moveToThread(self.alertThread)
        self.alertWorker.isRunning = True 

        self.alertThread.started.connect(AlertWorker.getAlertList)
        self.alertThread.started.connect(self.alertWorker.processAlerts)
        self.alertWorker.sigShowBuyOrderWidget.connect(self.showBuyOrderWidget)
        self.alertWorker.sigShowSellOrderWidget.connect(self.showSellOrderWidget)

        #worker to fetch holdings details
        self.holdingsFetchingWorker = HoldingsWorker(self.userDetails.apiKey, self.userDetails.apiSecretKey, self.userDetails.brCode)

        #Thread to fetch holdings continuously
        self.holdingsFetchingThread = QThread()
        self.holdingsFetchingWorker.moveToThread(self.holdingsFetchingThread)

        self.holdingsFetchingThread.started.connect(self.holdingsFetchingWorker.fetchHoldings)

        #worker to process holdings 
        self.holdingsProcessWorker = HoldingsWorker(profitTh= self.userDetails.profitThreshold, avgTh=self.userDetails.averageThreshold, desktopNoti=self.userDetails.deskNoti, teleNoti=self.userDetails.teleNoti)
        self.holdingsProcessWorker.sigHoldDetails.connect(self.showHoldingDetails)
        #Thread to process holdings
        self.holdingsProcessThread = QThread()
        self.holdingsProcessWorker.moveToThread(self.holdingsProcessThread)
        self.holdingsProcessThread.started.connect(self.holdingsProcessWorker.processHoldings)
        
        #worker to fetch MyOrders 
        self.myOrdersFetchingWorker = MyOrdersWorker(self.userDetails.apiKey, self.userDetails.apiSecretKey, self.userDetails.brCode)
        self.myOrdersFetchingWorker.sigMyOrdersDetails.connect(self.showMyOrdersDetails)
        #Thread to fetching MyOrders
        self.myOrdersFetchingThread = QThread()
        self.myOrdersFetchingWorker.moveToThread(self.myOrdersFetchingThread)
        self.myOrdersFetchingThread.started.connect(self.myOrdersFetchingWorker.fetchMyOrders)



        self.loop = asyncio.new_event_loop() 
        self.teleApiWorker = TeleApiWorker(self.loop)
        self.teleApiThread = QThread() #this thread runs event loop required to send message on telegram
        self.teleApiWorker.moveToThread(self.teleApiThread)

        self.teleApiThread.started.connect(self.teleApiWorker.startEventLoop)
        self.teleApiWorker.finished.connect(self.teleApiThread.quit)
        self.teleApiWorker.finished.connect(self.teleApiWorker.deleteLater)
        self.teleApiThread.finished.connect(self.teleApiThread.deleteLater)
        self.teleApiThread.finished.connect(lambda: print('thread finished completely'))
        

        self.specialAlertWorker = SpecialAlertsWorker(self.userDetails.deskNoti, self.userDetails.teleNoti)
        self.specialAlertThread = QThread()
        self.specialAlertWorker.moveToThread(self.specialAlertThread)

        self.specialAlertThread.started.connect(self.specialAlertWorker.getStkSymbolsList)
        self.specialAlertThread.started.connect(self.specialAlertWorker.check)

        self.teleApiThread.start()
        self.holdingsFetchingThread.start()
        self.holdingsProcessThread.start()
        self.alertThread.start() #this thread should be started later than the teleApiThread
        self.specialAlertThread.start()
        self.myOrdersFetchingThread.start()


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
            self.stkDetails.append(StockDetails(self.userDetails.userName, stkSym, stkName)) 
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
        self.specialAlerts.append(SpecialAlerts())
        self.specialAlerts[-1].show()

    def showMyOrdersWindow(self):
        self.myOrders.append(MyOrders(self.userDetails.userName)) 

    def showHoldingsWindow(self):
        self.holdings.append(Holdings()) 
        self.holdings[-1].show()
    
    def showWatchlistsWindow(self):
        self.watchlists = Watchlists()
        self.watchlists.show()
      
    def showCustomDetailsWindow(self):
        self.customDetails = CustomDetails(self.userDetails.userName)
        self.customDetails.ui.btnSave.clicked.connect(self.userDetails.getUserDetails)
        self.customDetails.ui.btnSave.clicked.connect(self.changeWorkerDetails)
        self.customDetails.show()

    '''method called when user clicks on buy button of notification sent on windows'''
    def showBuyOrderWidget(self, stkSymbol): 
        print('buyOrderWidget shown')
        self.orderWidget = BuyOrderDlg(stkSymbol)
        self.orderWidget.show()

    '''method called when user clicks on sell button of notification sent on windows'''
    def showSellOrderWidget(self): 
        self.orderWidget = SellOrderDlg(self.userDetails.userName)
        self.orderWidget.show()

    def showHoldingDetails(self, holdDetails):
        self.ui.lblTotalInvVal.setText(str(round(holdDetails['investedValue'].iloc[0], 2)))
        self.ui.lbalCurrentValueVal.setText(str(round(holdDetails['currentValue'].iloc[0], 2)))
        self.ui.lblPandLVal.setText(str(round(holdDetails['profitAndLoss'].iloc[0], 2)))

    def showMyOrdersDetails(self, myOrdersDetails):
        self.ui.lblPendingsVal.setText(str(myOrdersDetails['pendingOrdersCnt'].iloc[0]))
        self.ui.lblClosedVal.setText(str(myOrdersDetails['closedOrdersCnt'].iloc[0]))
        self.ui.lblRejectedVal.setText(str(myOrdersDetails['rejectedOrdersCnt'].iloc[0]))
    
    def changeWorkerDetails(self):
        self.holdingsFetchingWorker.changeDetails(self.userDetails.apiKey, self.userDetails.apiSecretKey, self.userDetails.brCode) 
        self.holdingsProcessWorker.changeDetails(profitTh= self.userDetails.profitThreshold, avgTh = self.userDetails.averageThreshold, desktopNoti= self.userDetails.deskNoti, teleNoti= self.userDetails.teleNoti)

        self.myOrdersFetchingWorker.changeDetails(self.userDetails.apiKey, self.userDetails.apiSecretKey, self.userDetails.brCode)
        self.alertWorker.changeDetails(self.userDetails.deskNoti, self.userDetails.teleNoti)
        self.specialAlertWorker.changeDetails(self.userDetails.deskNoti, self.userDetails.teleNoti)