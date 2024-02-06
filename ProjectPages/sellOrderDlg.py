from PySide6.QtWidgets import QDialog

from algomojo.pyapi import *
from UIFiles.ui_orderDlg import Ui_OrderDlg
from ProjectPages.messageDlg import MessageDlg

import pandas as pd
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


class SellOrderDlg(QDialog):
    def __init__(self, stkSymbol, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDlg()
        self.ui.setupUi(self)
        self.stkSymbol = stkSymbol
        self.ui.lblStkSymbol.setText(stkSymbol)
        self.ui.btnOrder.setText('SELL')
        self.ui.btnOrder.setDisabled(True)

        self.addConnectors()
        self.userDetails = UserDetails()
        self.accessApi()
        self.getHoldings()
        self.setQuantity()

    def addConnectors(self):
        self.ui.sbQuantity.valueChanged.connect(self.validateQuantity)
        self.ui.btnOrder.clicked.connect(self.close)
        self.ui.btnOrder.clicked.connect(self.placeSellOrder)

    def accessApi(self):
        self.algomojo = api(api_key = self.userDetails.apiKey, api_secret= self.userDetails.apiSecretKey)

    def getHoldings(self):
        self.holdings = json.loads(json.dumps(self.algomojo.Holdings('tc')))
        '''holdings = {"status": "success",
                        "data":[
                            {"exchange": "NSE",
                                "token": "3478273",
                                "symbol": "5PAISA",
                                "isin": "INE731H01025",
                                "holdqty": 150,
                                "btst_qty": 0,
                                "sellable_qty": 0,
                                "average_price": 323.6,
                                "ltp": 31.85,
                                "product": "CNC",
                                "coll_qty": 0,
                                "coll_type": "",
                                "invest_val": 47377.5,
                                "hld_val": 47377.5,
                                "PL": 0,
                                "broker_exchange": "BSE",
                                "broker_token": "3478273",
                                "tick_size": 0,
                                "lot_size": 0,
                                "holdtype": "HLD",
                                # "ws_msg": {
                                #     "exchange": "BSE",
                                #     "token": "3478273"
                                # }
                            },
                            {"exchange": "NSE",
                                "token": "3478273",
                                "symbol": "PNB-EQ",
                                "isin": "INE731H01025",
                                "holdqty": 150,
                                "btst_qty": 0,
                                "sellable_qty": 0,
                                "average_price": 323.6,
                                "ltp": 31.85,
                                "product": "CNC",
                                "coll_qty": 0,
                                "coll_type": "",
                                "invest_val": 47377.5,
                                "hld_val": 47377.5,
                                "PL": 0,
                                "broker_exchange": "BSE",
                                "broker_token": "3478273",
                                "tick_size": 0,
                                "lot_size": 0,
                                "holdtype": "HLD",
                                # "ws_msg": {
                                #     "exchange": "BSE",
                                #     "token": "3478273"
                                # }
                            }]
                        }'''
        self.holdings = pd.DataFrame(self.holdings['data'])

    def setQuantity(self):
        self.stkHoldingDetails = self.holdings.loc[self.holdings['symbol'] == self.stkSymbol+'-EQ']
        print(self.stkHoldingDetails)

        if(self.stkHoldingDetails.size == 0):
            self.ui.lblAvailQuantityVal.setText('0')
        else:
            self.ui.lblAvailQuantityVal.setText(str(self.stkHoldingDetails['holdqty'].iloc[0]))

    
    def validateQuantity(self):
        #fetch quantity using api call

        #check if quantiy is less than or equal to available quantiy
        if(self.stkHoldingDetails.size == 0):
            holdingQuantity = 0
        else:
            holdingQuantity = self.stkHoldingDetails['holdqty'].iloc[0]

        if(self.ui.sbQuantity.value() == 0 or self.ui.sbQuantity.value() > holdingQuantity):
            self.ui.btnOrder.setDisabled(True)
        else: 
            self.ui.btnOrder.setEnabled(True)

    
    def setOrderDetails(self, order):
        self.ui.sbQuantity.setValue(order['quantity'])
        self.ui.cmbPriceType.setCurrentText(order['pricetype'])
        self.ui.dsbPriceValue.setValue(order['price'])

    def placeSellOrder(self):
        broker = 'tc'
        strategy = 'MyStrategy'
        exchange = 'NSE'
        symbol = self.ui.lblStkSymbol.text()+'-EQ'
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

    def modifyOrder(self, order):
            self.algomojo = api(api_key = self.userDetails.apiKey, api_secret= self.userDetails.apiSecretKey)

            broker = 'tc'
            strategy = 'MyStrategy'
            exchange = 'NSE'
            symbol = order['symbol'][0]
            action = order['action'][0]
            product = order['product'][0]
            priceType = self.ui.cmbPriceType.currentText()
            quantity = self.ui.sbQuantity.value()
            price = self.ui.dsbPriceValue.value()
            order_id = order['order_id']

            try:
                responseDict = self.algomojo.ModifyOrder(broker = broker, strategy = strategy, symbol = symbol, order_id= order_id, action = action, product = product, pricetype= priceType, quantity= quantity, price = price, exchange= exchange)

                self.msgDlg = MessageDlg('')
                if(responseDict['status'] == 'success'):
                    self.msgDlg.ui.lblMsg.setText('order modified successfully......')
                    print('order modified successfully......')
                else:
                    self.msgDlg.ui.lblMsg.setText('Order can not be modified due to ' + responseDict['error_msg'])
                    print('Order can not be modified due to', responseDict['error_msg'])

                self.msgDlg.show()
            except Exception as e: 
                print(e)
