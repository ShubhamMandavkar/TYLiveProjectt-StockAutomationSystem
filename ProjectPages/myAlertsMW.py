from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QMainWindow

import mysql.connector
from mysql.connector import errorcode
from UIFiles.ui_myAlerts import Ui_myAlerts


class ListModel(QAbstractListModel):
    def __init__(self, data=None):
        super(ListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            *_ ,text = self._data[index.row()]
            # Return the todo text only.
            return text

    def rowCount(self, index):
        return len(self._data)    

class MyAlerts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_myAlerts()
        self.ui.setupUi(self)

        self.addConnectors()
        self.addAlertsToList()
    
    def addConnectors(self):
        self.ui.btnDelete.clicked.connect(self.deleteAlert)  

    def deleteAlert(self):
        modelIndexls = self.ui.lsvMyAlerts.selectedIndexes()
        row = modelIndexls[0].row()
        alert = self.ui.lsvMyAlerts.model()._data[row]

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #delete alert from table
            query = f"""delete from alerts where stkSymbol = '{alert[0]}' and alertType = '{alert[2]}' and alertCondition = '{alert[3]}' and timeFrame = '{alert[4]}' and alertVal = {alert[5]} and len1 = {alert[6]} and len2 = {alert[7]}"""
            print(query)
            cursor.execute(query)
            con.commit()

            #get the updated records in alert table
            query = f"""select * from alerts"""
            cursor.execute(query)

            data = []
            for (symbol,name, type, cond, tf, val, len1, len2, msg) in cursor: #cursor returns tuple
                string = name + ' ' + cond + ' ' + str(val)
                data.append([symbol, name, type, cond, tf, val, len1, len2, msg, string])

            model = ListModel(data)    
            self.ui.lsvMyAlerts.setModel(model)
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

    def addAlertsToList(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #get the value of stkSymbol
            query = f"""select * from alerts"""
            cursor.execute(query)

            data = []
            for (symbol,name, type, cond, tf, val,len1, len2, msg) in cursor: #cursor returns tuple
                string = name + ' ' + cond + ' ' + str(val)
                data.append([symbol, name, type, cond, tf, val, len1, len2, msg, string])

            model = ListModel(data)    
            self.ui.lsvMyAlerts.setModel(model) 

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
