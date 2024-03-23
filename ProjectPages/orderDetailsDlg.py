from PySide6.QtWidgets import QDialog
from ProjectPages.messageDlg import MessageDlg
from UIFiles.ui_orderDetailsDlg import Ui_OrderDetailsDlg
from ProjectPages.buyOrderDlg import BuyOrderDlg
from ProjectPages.sellOrderDlg import MyException, SellOrderDlg

from algomojo.pyapi import *

import mysql.connector
from mysql.connector import errorcode

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

class OrderDetailsDlg(QDialog):
    def __init__(self, userName, order, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDetailsDlg()
        self.ui.setupUi(self)
        self.setWindowTitle('Order')
        self.order = order
        self.userName = userName
        self.userDetails = UserDetails(userName)

        self.setDetails()
        if(self.order['status'] != 'open' and self.order['status'] != 'pending'):
            self.hideButtonsFrame()

        self.addConnectors()

    def addConnectors(self):
        self.ui.btnCancel.clicked.connect(self.cancelOrder)
        self.ui.btnModify.clicked.connect(self.modifyOrder)
        self.ui.btnModify.clicked.connect(self.close)

    def setDetails(self):
        self.ui.lblStkSymbol.setText(self.order['symbol'])
        self.ui.lblQuantityVal.setText(str(int(self.order['quantity'])) + ' shares')
        self.ui.lblOrderTypeVal.setText(self.order['action'] + ', '+ self.order['product'])
        if(self.order['pricetype'] == 'MARKET'):
            self.ui.lblOrderPriceVal.setText(self.order['pricetype'] + 'price')
        else:
            self.ui.lblOrderPriceVal.setText(str(self.order['price']))

        self.ui.lblAvgPriceVal.setText(str(self.order['avgprc']))
        self.ui.lblExchangeVal.setText(self.order['exchange'])

        if(self.order['status'] == 'completed'):
            self.ui.lblOrderStatusVal.setText('successful')
        elif(self.order['status'] == 'rejected'):
            self.ui.lblOrderStatusVal.setText('failed')
        else:
            self.ui.lblOrderStatusVal.setText(self.order['status'])

        self.ui.lblReqReceivedVal.setText(self.order['orderentrytime'])
        self.ui.lblOrderIdVal.setText(self.order['order_id'])
        self.ui.lblOrderPlacedVal.setText(self.order['exchconfrmtime'])
        self.ui.lblExchOrderIdVal.setText(self.order['exchordid'])

    def modifyOrder(self):
        symbol , _ = self.order['symbol'].split('-')
        if(self.order['action'] == 'BUY'):
            self.orderDlg = BuyOrderDlg(self.userName, symbol)
            self.orderDlg.setOrderDetails(self.order)
            self.orderDlg.ui.btnOrder.clicked.disconnect(self.orderDlg.placeBuyOrder)
            self.orderDlg.ui.btnOrder.clicked.connect(lambda:self.orderDlg.modifyOrder(self.order))
            self.orderDlg.show()
            print('Modified buy order')
        else:
            try:
                self.orderDlg = SellOrderDlg(self.userName, symbol)
                self.orderDlg.setOrderDetails(self.order)
                self.orderDlg.validateQuantity()
                self.orderDlg.ui.btnOrder.clicked.disconnect(self.orderDlg.placeSellOrder)
                self.orderDlg.ui.btnOrder.clicked.connect(lambda:self.orderDlg.modifyOrder(self.order))
                self.orderDlg.show()
                print('Modified sell order')
            except MyException as e:
                self.msgDlg = MessageDlg(e.msg)
                self.msgDlg.show()
                print(e)

    def cancelOrder(self):
        self.algomojo = api(api_key = self.userDetails.apiKey, api_secret= self.userDetails.apiSecretKey)
        
        try:
            responseDict = self.algomojo.CancelOrder(self.userDetails.brCode, self.order["order_id"])

            if(responseDict['status'] == 'success'):
                self.showMessage('order placed successfully......')
                print('order placed successfully......')
            else:
                self.showMessage('Order can not be placed due to ' + responseDict['error_msg'])
                print('Order can not be placed due to', responseDict['error_msg'])

        except requests.exceptions.ConnectionError:
            self.showMessage('Please check your internet connection')
        except Exception as e:
            print(e)
            self.showMessage(str(e))
        
        self.close()

    def showMessage(self, msg):
        self.msgDlg = MessageDlg(msg)
        self.msgDlg.show()

    def hideButtonsFrame(self):
        self.ui.frmButtons.hide()