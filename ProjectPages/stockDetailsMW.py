from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow

from workers import StockWorker
from APIMethods import getQuote2, getQuote, getQuoteFromYfinance
import json

from UIFiles.ui_stockDetails import Ui_stockDetails
from ProjectPages.alertDlg import AlertDlg
from ProjectPages.chartMW import Chart
from ProjectPages.messageDlg import MessageDlg
from ProjectPages.buyOrderDlg import BuyOrderDlg
from ProjectPages.sellOrderDlg import SellOrderDlg

class StockDetails(QMainWindow):
    def __init__(self, stkSym, stkName, parent=None):
        super().__init__(parent)
        self.ui = Ui_stockDetails()
        self.ui.setupUi(self)
        self.ui.lblChange.hide()
        self.ui.lblChangeVal.hide()

        self.stkSymbol = stkSym
        self.stkName = stkName

        self.ui.lblStkName.setText(self.stkName)
        self.ui.lblSymbolVal.setText(self.stkSymbol)

        self.addConnectors()
        
        self.stockWorker = StockWorker(self.stkSymbol)
        self.stockThread = QThread()
        self.stockWorker.moveToThread(self.stockThread)

        self.stockThread.started.connect(self.stockWorker.fetchStockDetails)   
        self.stockWorker.sigShowStkDetails.connect(self.showStkDetails)
        self.stockWorker.sigShowMsg.connect(self.showMessage)
        '''the below thread.quit() and thread.wait() needs to be called to properly quit the thread'''
        self.stockWorker.finished.connect(self.stockThread.quit) 
        self.stockWorker.finished.connect(self.stockThread.wait)
        self.stockWorker.finished.connect(self.stockWorker.deleteLater)
        self.stockThread.finished.connect(self.stockThread.deleteLater)
        self.stockThread.start()


    def addConnectors(self):
        self.ui.btnAlert.clicked.connect(self.showAlertDialog)
        self.ui.btnChart.clicked.connect(self.showChartWindow)
        self.ui.btnBuy.clicked.connect(self.showBuyOrderWidget)
        self.ui.btnSell.clicked.connect(self.showSellOrderWidget)

    def showDetails(self):
        stk = json.loads(getQuote2('',self.stkSymbol, 'tc', 'NSE'))
        self.ui.lblSymbolVal.setText(self.stkSymbol)
        self.ui.lblCompanyVal.setText(stk['data']['company_name'])
        self.ui.lblExchangeVal.setText(stk['data']['exchange'])
        self.ui.lblOpenVal.setText(str(stk['data']['open']))
        self.ui.lblHighVal.setText(str(stk['data']['high']))
        self.ui.lblLowVal.setText(str(stk['data']['low']))
        self.ui.lblCloseVal.setText(str(stk['data']['close']))
        self.ui.lblChangeVal.setText(str(stk['data']['change']))
        self.ui.lbl52wkHighVal.setText(str(stk['data']['yearly_high_price']))
        self.ui.lbl52wkLowVal.setText(str(stk['data']['yearly_low_price']))
        self.ui.lblVolumeVal.setText(str(stk['data']['volume']))

    def showStkDetails(self, stkDf):
        self.ui.lblCompanyVal.setText(self.stkName)
        self.ui.lblExchangeVal.setText('NSE')
        self.ui.lblOpenVal.setText(str(round(stkDf['Open'].iloc[0], 2)))
        self.ui.lblHighVal.setText(str(round(stkDf['High'].iloc[0], 2)))
        self.ui.lblLowVal.setText(str(round(stkDf['Low'].iloc[0], 2)))
        self.ui.lblCloseVal.setText(str(round(stkDf['Close'].iloc[0], 2)))
        self.ui.lblVolumeVal.setText(str(stkDf['Volume'].iloc[0]))

        self.ui.lbl52wkHighVal.setText(str(stkDf['fiftyTwoWeekHigh'].iloc[0]))
        self.ui.lbl52wkLowVal.setText(str(stkDf['fiftyTwoWeekLow'].iloc[0]))

    def showBuyOrderWidget(self):
        self.orderWidget = BuyOrderDlg(self.stkSymbol)
        self.orderWidget.show()
    
    def showSellOrderWidget(self):
        self.orderWidget = SellOrderDlg(self.stkSymbol)
        self.orderWidget.show()
    
    def showAlertDialog(self):
        self.dlgAlert = AlertDlg(self.stkSymbol, self.stkName)

        # stk = json.loads(getQuote2("shubh", self.stkName, 'tc', 'NSE'))
        # lastPrice = stk['data']['last_price']
        try:
            stkDf = getQuoteFromYfinance('shubh',self.stkSymbol, 'tc', 'NSE')
            lastPrice = stkDf['Close'].iloc[-1]
        except Exception as e:
            lastPrice = 0.00
            print('Please check your internet connection')
            
        self.dlgAlert.ui.dsbAlertVal.setValue(lastPrice)
        self.dlgAlert.show()

    def showChartWindow(self):
        self.chart = Chart(self.stkSymbol, self.stkName)
        self.chart.show()

    def showMessage(self, msg):
        self.msgDlg = MessageDlg(msg)
        self.msgDlg.show()

    def closeEvent(self, event):
        print('closing stockDetails Window')
        self.stockWorker.isRunning = False
        event.accept()
        print('closed stockDetails Window')

    