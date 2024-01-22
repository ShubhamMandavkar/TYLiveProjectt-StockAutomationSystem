from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QAbstractListModel, Qt
import mysql.connector
from mysql.connector import errorcode
from algomojo.pyapi import *
import pandas as pd

from UIFiles.ui_myOrders import Ui_myOrders
from ProjectPages.orderDetailsDlg import OrderDetailsDlg


class ListModel(QAbstractListModel):
    def __init__(self, data=None):
        super(ListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            name = self._data['symbol'][index.row()]
            quantity = self._data['quantity'][index.row()]
            action = self._data['action'][index.row()]
            return str(name +' . '+ str(int(quantity)) +' . '+ action)

    def rowCount(self, index):
        return len(self._data)  


class UserDetails:
    def __init__(self):
        self.apiKey = ''
        self.apiSecretKey = ''
    
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

def fetchAllOrders(userDetails):
    try:
        algomojo = api(api_key = userDetails.apiKey, api_secret= userDetails.apiSecretKey)

        orders = algomojo.OrderBook(broker='tc')
        return orders
    except Exception as e:
        print(e)

    return {"status": "error"}

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
            "action": "BUY",
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_myOrders()
        self.ui.setupUi(self)

        self.userDetails = UserDetails()
        self.userDetails.getUserDetails()
        self.addConnectors()

        self.loadAllOrders()

    def addConnectors(self):
        self.ui.lsvAllOrders.doubleClicked.connect(self.showOrderDetails)
        self.ui.lsvPendingOrders.doubleClicked.connect(self.showPendingOrderDetails)

    
    def loadAllOrders(self):
        self.myOrders = fetchAllOrders2(self.userDetails)

        if(self.myOrders['status'] == 'success'):
            orders = pd.DataFrame(self.myOrders['data'])
            orders.drop(['ws_msg'], axis = 1, inplace= True)

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

            pendingOrdersModel = ListModel(pendingOrders)
            self.ui.lsvPendingOrders.setModel(pendingOrdersModel)
        else:
            print(self.myOrders['error_msg'])

    def showOrderDetails(self):
        modelIndexls = self.ui.lsvAllOrders.selectedIndexes()
        row = modelIndexls[0].row()
        order = self.ui.lsvAllOrders.model()._data.iloc[row]

        self.orderDetails = OrderDetailsDlg(order)
        self.orderDetails.show()

    def showPendingOrderDetails(self):
        modelIndexls = self.ui.lsvPendingOrders.selectedIndexes()
        row = modelIndexls[0].row()
        order = self.ui.lsvPendingOrders.model()._data.iloc[row]

        self.orderDetails = OrderDetailsDlg(order)
        self.orderDetails.show()