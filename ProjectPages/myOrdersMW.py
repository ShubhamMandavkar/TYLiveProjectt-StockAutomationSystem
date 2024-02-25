from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QAbstractListModel, Qt, QThread
import mysql.connector
from mysql.connector import errorcode
from algomojo.pyapi import *
import pandas as pd
from ProjectPages.messageDlg import MessageDlg

from UIFiles.ui_myOrders import Ui_myOrders
from ProjectPages.orderDetailsDlg import OrderDetailsDlg
from workers import MyOrdersWorker


class ListModel(QAbstractListModel):
    def __init__(self, data=None):
        super(ListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            date = self._data['exchconfrmtime'][index.row()]
            name = self._data['symbol'][index.row()]
            quantity = self._data['quantity'][index.row()]
            action = self._data['action'][index.row()]
            return str(date + '\n' + name +' . '+ str(int(quantity)) +' . '+ action)

    def rowCount(self, index):
        return len(self._data)  

class UserDetails:
    def __init__(self, userName):
        self.userName = userName
        self.apiKey = ''
        self.apiSecretKey = ''
    
    def getUserDetails(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select apiKey, apiSecretKey from customer_details where userId = '{self.userName}'"""
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

def fetchAllOrders2(userDetails):
    orders = {
        "status": "success",
        "data": [
            {
            "exchange": "NSE",
            "token": "11915",
            "symbol": "YESBANK-EQ",
            "product": "CNC",
            "pricetype": "MARKET",
            "Ret": "DAY",
            "price": 0,
            "trigger_price": 0,
            "quantity": 1,
            "disclosed_quantity": 0,
            "action": "BUY",
            "avgprc": 13.95,
            "fillshares": 1,
            "remarks": "ARROW",
            "exchordid": "1300000016630228",
            "parentorderid": "",
            "order_id": "220113000041330",
            "orderentrytime": "Jan 13 2022 13:24:00",
            "exchconfrmtime": "13-Jan-2022 13:24:00",
            "status": "rejected",
            "ordvaldate": "",
            "rejreason": "",
            "broker_exchange": "NSE",
            "broker_token": "14366",
            "tick_size": 0.05,
            "lot_size": 1,
            "ws_msg": {
                "exchange": "NSE",
                "token": "14366"
            }
        }, 
        {
            "exchange": "NSE",
            "token": "11915",
            "symbol": "INFY-EQ",
            "product": "CNC",
            "pricetype": "MARKET",
            "Ret": "DAY",
            "price": 0,
            "trigger_price": 0,
            "quantity": 1,
            "disclosed_quantity": 0,
            "action": "BUY",
            "avgprc": 13.95,
            "fillshares": 1,
            "remarks": "ARROW",
            "exchordid": "1300000016630228",
            "parentorderid": "",
            "order_id": "220113000041330",
            "orderentrytime": "Jan 13 2022 13:24:00",
            "exchconfrmtime": "13-Jan-2022 13:24:00",
            "status": "completed",
            "ordvaldate": "",
            "rejreason": "",
            "broker_exchange": "NSE",
            "broker_token": "14366",
            "tick_size": 0.05,
            "lot_size": 1,
            "ws_msg": {
                "exchange": "NSE",
                "token": "14366"
            }
        }, 
        {
            "exchange": "NSE",
            "token": "11915",
            "symbol": "INFY-EQ",
            "product": "CNC",
            "pricetype": "MARKET",
            "Ret": "DAY",
            "price": 0,
            "trigger_price": 0,
            "quantity": 1,
            "disclosed_quantity": 0,
            "action": "BUY",
            "avgprc": 13.95,
            "fillshares": 1,
            "remarks": "ARROW",
            "exchordid": "1300000016630228",
            "parentorderid": "",
            "order_id": "220113000041330",
            "orderentrytime": "Jan 13 2022 13:24:00",
            "exchconfrmtime": "13-Jan-2022 13:24:00",
            "status": "open",
            "ordvaldate": "",
            "rejreason": "",
            "broker_exchange": "NSE",
            "broker_token": "14366",
            "tick_size": 0.05,
            "lot_size": 1,
            "ws_msg": {
                "exchange": "NSE",
                "token": "14366"
            }
        }, 
        {
            "exchange": "NSE",
            "token": "11915",
            "symbol": "PNB-EQ",
            "product": "CNC",
            "pricetype": "MARKET",
            "Ret": "DAY",
            "price": 0,
            "trigger_price": 0,
            "quantity": 1,
            "disclosed_quantity": 0,
            "action": "SELL",
            "avgprc": 13.95,
            "fillshares": 1,
            "remarks": "ARROW",
            "exchordid": "1300000016630228",
            "parentorderid": "",
            "order_id": "220113000041330",
            "orderentrytime": "Jan 13 2022 13:24:00",
            "exchconfrmtime": "13-Jan-2022 13:24:00",
            "status": "pending",
            "ordvaldate": "",
            "rejreason": "",
            "broker_exchange": "NSE",
            "broker_token": "14366",
            "tick_size": 0.05,
            "lot_size": 1,
            "ws_msg": {
                "exchange": "NSE",
                "token": "14366"
            }
        }]
    }
    return orders


class MyOrders(QMainWindow):
    def __init__(self, userName,  parent=None):
        super().__init__(parent)
        self.ui = Ui_myOrders()
        self.ui.setupUi(self)
        self.setWindowTitle('My Orders')
        self.ui.lsvAllOrders.hide()
        self.ui.lsvPendingOrders.hide()

        self.userDetails = UserDetails(userName)
        self.userDetails.getUserDetails()

        self.addConnectors()
        self.show()  #show the gui window

        #worker to fetch MyOrders 
        self.myOrdersWorker = MyOrdersWorker()
        #Thread for fetching MyOrders
        self.myOrdersThread = QThread()
        self.myOrdersWorker.moveToThread(self.myOrdersThread)
        self.myOrdersWorker.isMyOrdersPage = True

        self.myOrdersThread.started.connect(self.myOrdersWorker.getMyOrdersTableModel)
        '''the below thread.quit() and thread.wait() needs to be called to properly quit the thread'''
        self.myOrdersWorker.finished.connect(self.myOrdersThread.quit)
        self.myOrdersWorker.finished.connect(self.myOrdersThread.wait)
        self.myOrdersWorker.finished.connect(self.myOrdersWorker.deleteLater)
        self.myOrdersThread.finished.connect(self.myOrdersThread.deleteLater)

        self.myOrdersWorker.sigChngMyOrdersData.connect(self.showOrders)
        self.myOrdersWorker.sigShowMsg.connect(self.showMessage)
        self.myOrdersThread.start()

    def addConnectors(self):
        self.ui.lsvAllOrders.doubleClicked.connect(self.showOrderDetails)
        self.ui.lsvPendingOrders.doubleClicked.connect(self.showPendingOrderDetails)
    
    def showOrders(self, orders):
        if(len(orders) != 0):
            self.ui.lblNoOrders.hide()
            self.ui.lsvAllOrders.setVisible(True)

            successfulOrders = orders['status'] == 'completed'
            rejectedOrders = orders['status'] == 'rejected'
            cancelledOrders = orders['status'] == 'cancelled'
            pendingOrders = orders['status'] == 'pending'
            openOrders = orders['status'] == 'open'

            # allOrders = orders.where(successfulOrders | rejectedOrders | cancelledOrders) #filter successful or rejected orders
            allOrders = orders
            # allOrders = orders.where(successfulOrders)  
            allOrders.dropna(axis= 0, inplace= True) #after filtering the resultant df will place Na values in place of other records threfore remove records containing na values
            allOrders.reset_index(inplace=True) #reset the index after removing records with na values

            allOrdersModel = ListModel(allOrders)
            self.ui.lsvAllOrders.setModel(allOrdersModel)

            pendingOrders = orders.where(pendingOrders | openOrders) #filter open or pending orders
            # allOrders = orders.where(successfulOrders)  
            pendingOrders.dropna(axis= 0, inplace= True) #after filtering the resultant df will place Na values in place of other records threfore remove records containing na values
            pendingOrders.reset_index(inplace=True) #reset the index after removing records with na values

            if(len(pendingOrders) != 0):
                self.ui.lblNoPendingOrders.hide()
                self.ui.lsvPendingOrders.setVisible(True)
                
                pendingOrdersModel = ListModel(pendingOrders)
                self.ui.lsvPendingOrders.setModel(pendingOrdersModel)
            else:
                self.ui.lblNoPendingOrders.setVisible(True)
                self.ui.lsvPendingOrders.hide()
        else:
            self.ui.lblNoOrders.setVisible(True)
            self.ui.lsvAllOrders.hide()

            self.ui.lblNoPendingOrders.setVisible(True)
            self.ui.lsvPendingOrders.hide()

    def showOrderDetails(self):
        modelIndexls = self.ui.lsvAllOrders.selectedIndexes()
        row = modelIndexls[0].row()
        order = self.ui.lsvAllOrders.model()._data.iloc[row]

        self.orderDetails = OrderDetailsDlg(self.userDetails.userName, order)
        self.orderDetails.show()

    def showPendingOrderDetails(self):
        modelIndexls = self.ui.lsvPendingOrders.selectedIndexes()
        row = modelIndexls[0].row()
        order = self.ui.lsvPendingOrders.model()._data.iloc[row]

        self.orderDetails = OrderDetailsDlg(self.userDetails.userName, order)
        self.orderDetails.show()

    def showMessage(self, msg):
        self.msgDlg = MessageDlg(msg)
        self.msgDlg.show()

    def closeEvent(self, event):
        print('closing myOrders window')
        self.myOrdersWorker.isMyOrdersPage = False
        event.accept()
        print('called closeWindow')