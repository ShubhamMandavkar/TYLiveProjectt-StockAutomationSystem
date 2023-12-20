
from PySide6.QtWidgets import QMainWindow
from APIMethods import getQuote, getQuote2
import json
import yfinance as yf

from UIFiles.ui_stockDetails import Ui_stockDetails
from ProjectPages.alertDlg import AlertDlg
from ProjectPages.chartMW import Chart


class StockDetails(QMainWindow):
    def __init__(self, stkSym, stkName, parent=None):
        super().__init__(parent)
        self.ui = Ui_stockDetails()
        self.ui.setupUi(self)

        self.stkSymbol = stkSym
        self.stkName = stkName

        self.showDetails()
        self.addConnectors()

    def addConnectors(self):
        self.ui.btnAlert.clicked.connect(self.showAlertDialog)
        self.ui.btnChart.clicked.connect(self.showChartWindow)
        self.ui.btnBuy.clicked.connect(self.getBuyDetails)

    def showDetails(self):
        # stk = json.loads(getQuote2('',self.stkSymbol, 'tc', 'NSE'))
        self.ui.lblStkName.setText(self.stkName)
        self.ui.lblSymbolVal.setText(self.stkSymbol)
        # self.ui.lblCompanyVal.setText(stk['data']['company_name'])
        # self.ui.lblExchangeVal.setText(stk['data']['exchange'])
        # self.ui.lblOpenVal.setText(str(stk['data']['open']))
        # self.ui.lblHighVal.setText(str(stk['data']['high']))
        # self.ui.lblLowVal.setText(str(stk['data']['low']))
        # self.ui.lblCloseVal.setText(str(stk['data']['close']))
        # self.ui.lblChangeVal.setText(str(stk['data']['change']))
        # self.ui.lbl52wkHighVal.setText(str(stk['data']['yearly_high_price']))
        # self.ui.lbl52wkLowVal.setText(str(stk['data']['yearly_low_price']))
        # self.ui.lblVolumeVal.setText(str(stk['data']['volume']))

        stk = yf.Ticker(self.stkSymbol +".NS")
        stkInfo = stk.info
        self.ui.lblCompanyVal.setText(stkInfo['longName'])
        self.ui.lblExchangeVal.setText('NSE')
        self.ui.lblOpenVal.setText(str(stkInfo['open']))
        self.ui.lblHighVal.setText(str(stkInfo['dayHigh']))
        self.ui.lblLowVal.setText(str(stkInfo['dayLow']))
        self.ui.lblCloseVal.setText(str(stkInfo['previousClose']))
        self.ui.lblChange.hide()
        self.ui.lblChangeVal.hide()
        # self.ui.lblChangeVal.setText(str(stkInfo['longName']))
        self.ui.lbl52wkHighVal.setText(str(stkInfo['fiftyTwoWeekHigh']))
        self.ui.lbl52wkLowVal.setText(str(stkInfo['fiftyTwoWeekLow']))
        self.ui.lblVolumeVal.setText(str(stkInfo['volume']))

    def getBuyDetails(self):
        pass
    
    def showAlertDialog(self):
        self.dlgAlert = AlertDlg(self.stkSymbol, self.stkName)
        self.dlgAlert.show()
    
    def showChartWindow(self):
        self.chart = Chart(self.stkSymbol, self.stkName)
        self.chart.show()
    