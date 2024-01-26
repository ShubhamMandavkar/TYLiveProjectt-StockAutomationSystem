from PySide6.QtWidgets import QDialog

from algomojo.pyapi import *
from UIFiles.ui_orderDlg import Ui_OrderDlg
from ProjectPages.messageDlg import MessageDlg

import mysql.connector
from mysql.connector import errorcode

class UserDetails:
    def __init__(self):
        self.apiKey = ''
        self.apiSecretKey = ''
        self.getUserDetails()
    
    def getUserDetails(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
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


class BuyOrderDlg(QDialog):
    def __init__(self, stkSymbol, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDlg()
        self.ui.setupUi(self)

        self.ui.lblAvailQuantity.setVisible(False)
        self.ui.lblAvailQuantityVal.setVisible(False)
        self.ui.lblStkSymbol.setText(stkSymbol)
        self.ui.btnOrder.setText('BUY')

        self.addConnectors()
        self.userDetails = UserDetails()

    def addConnectors(self):
        self.ui.btnOrder.clicked.connect(self.close)
        self.ui.btnOrder.clicked.connect(self.placeBuyOrder)

    def placeBuyOrder(self):
        self.algomojo = api(api_key = self.userDetails.apiKey, api_secret= self.userDetails.apiSecretKey)

        broker = 'tc'
        strategy = 'MyStrategy'
        exchange = 'NSE'
        symbol = self.ui.lblStkSymbol.text()
        action = self.ui.btnOrder.text()
        product = 'CNC'
        priceType = self.ui.cmbPriceType.currentText()
        quantity = self.ui.sbQuantity.value()
        price = self.ui.dsbPriceValue.value()

        try:
            responseDict = self.algomojo.PlaceOrder(broker, exchange, symbol, action,product, quantity, priceType, strategy, price)

            self.msgDlg = MessageDlg('')
            if(responseDict['status'] == 'success'):
                self.msgDlg.ui.lblMsg.setText('order placed successfully......')
                print('order placed successfully......')
            else:
                self.msgDlg.ui.lblMsg.setText('Order can not be placed due to ' + responseDict['error_msg'])
                print('Order can not be placed due to', responseDict['error_msg'])

            self.msgDlg.show()
        except Exception as e:
            print(e)
