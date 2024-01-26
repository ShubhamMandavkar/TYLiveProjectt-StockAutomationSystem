from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QMainWindow

import mysql.connector
from mysql.connector import errorcode
from UIFiles.ui_myAlerts import Ui_myAlerts
from ProjectPages.alertDlg import AlertDlg
from workers import AlertWorker


class ListModel(QAbstractListModel):
    def __init__(self, data=None):
        super(ListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            *_ ,msg, _ = self._data[index.row()]
            # Return the todo text only.
            if(self._data[index.row()][9]):
                return msg + ' | Paused'
            return msg
    
    def changeMsgToPaused(self, row):
        self.layoutAboutToBeChanged.emit()
        self._data[row][8] = self._data[row][8] + ' | Paused'
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self._data)  

class EditAlertDlg(AlertDlg):
    def __init__(self, stkSym, stkName, parent=None):
        super().__init__(stkSym, stkName, parent)

    def fillAlertValues(self, alert):
        self.alert = alert
        self.ui.cmbAlertType.setCurrentText(alert[2])
        self.ui.cmbAlertCond.setCurrentText(alert[3])
        self.ui.cmbTimeFrame.setCurrentText(alert[4])
        self.ui.dsbAlertVal.setValue(alert[5])
        self.ui.sbLen1.setValue(alert[6])
        self.ui.sbLen2.setValue(alert[7])

    
    def addAlert(self):
        alertType = self.ui.cmbAlertType.currentText()
        alertCond = self.ui.cmbAlertCond.currentText()
        timeFrame = self.ui.cmbTimeFrame.currentText()
        alertVal = round(self.ui.dsbAlertVal.value(), 2)
        len1 = self.ui.sbLen1.value() 
        len2 = self.ui.sbLen2.value() 
        alertMsg = self.ui.txteMsg.toPlainText()   

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""update alerts set alertType = '{alertType}', alertCondition = '{alertCond}', timeFrame = '{timeFrame}', alertVal = {alertVal}, len1 = {len1}, len2 = {len2}, alertMsg = '{alertMsg}', isPaused = 0 where stkSymbol = '{self.stkSymbol}' and alertType = '{self.alert[2]}' and alertCondition = '{self.alert[3]}' and timeFrame = '{self.alert[4]}' and alertVal = {self.alert[5]} and len1 = {self.alert[6]} and len2 = {self.alert[7]}"""
            print(query)
            cursor.execute(query)
            con.commit()

            #add alert to alertlist in AlertWorker for processing
            AlertWorker.getAlertList()

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

        print("alert updated successfully")
        self.close()   #closes window when user successfully set alert

class MyAlerts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_myAlerts()
        self.ui.setupUi(self)

        self.addConnectors()
        self.addAlertsToList()
    
    def addConnectors(self):
        self.ui.btnDelete.clicked.connect(self.deleteAlert)  
        self.ui.lsvMyAlerts.doubleClicked.connect(self.editAlert)
        self.ui.btnPause.clicked.connect(self.pauseAlert)

    def editAlert(self):
        modelIndexls = self.ui.lsvMyAlerts.selectedIndexes()
        row = modelIndexls[0].row()
        alert = self.ui.lsvMyAlerts.model()._data[row]

        stkSymbol = alert[0]
        stkName = alert[1]
        self.dlgAlert = EditAlertDlg(stkSymbol, stkName)
        self.dlgAlert.fillAlertValues(alert)
        self.dlgAlert.ui.btnSetAlert.clicked.connect(self.addAlertsToList)  #after updating alert load all alerts 
        self.dlgAlert.show()
    
        
    def pauseAlert(self):
        modelIndexls = self.ui.lsvMyAlerts.selectedIndexes()
        row = modelIndexls[0].row()
        alert = self.ui.lsvMyAlerts.model()._data[row]
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #get the values of alert
            query = f"""select isPaused from alerts where stkSymbol = '{alert[0]}' and alertType = '{alert[2]}' and alertCondition = '{alert[3]}' and timeFrame = '{alert[4]}' and alertVal = {alert[5]} and len1 = {alert[6]} and len2 = {alert[7]}"""
            cursor.execute(query)

            for (isPaused,) in cursor: #cursor returns tuple
                print(isPaused)
                if(isPaused):
                    return

            #update the values of alert
            query = f"""update alerts set isPaused = 1 where stkSymbol = '{alert[0]}' and alertType = '{alert[2]}' and alertCondition = '{alert[3]}' and timeFrame = '{alert[4]}' and alertVal = {alert[5]} and len1 = {alert[6]} and len2 = {alert[7]}"""
            cursor.execute(query)
            con.commit()
            print('alert paused')
            self.model.changeMsgToPaused(row)
            AlertWorker.getAlertList()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            con.close()

    def deleteAlert(self):
        modelIndexls = self.ui.lsvMyAlerts.selectedIndexes()
        row = modelIndexls[0].row()
        alert = self.ui.lsvMyAlerts.model()._data[row]

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #delete alert from table
            query = f"""delete from alerts where stkSymbol = '{alert[0]}' and alertType = '{alert[2]}' and alertCondition = '{alert[3]}' and timeFrame = '{alert[4]}' and alertVal = {alert[5]} and len1 = {alert[6]} and len2 = {alert[7]}"""
            print(query)
            cursor.execute(query)
            con.commit()

            #get the updated records in alert table
            self.addAlertsToList()

            #After deleting the alert get updated list
            AlertWorker.getAlertList()

            cursor.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            con.close()

    def addAlertsToList(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #get the value of stkSymbol
            query = f"""select * from alerts"""
            cursor.execute(query)

            data = []
            for (symbol, name, type, cond, tf, val,len1, len2, msg, isPaused, lastTriggerTime) in cursor: #cursor returns tuple
                data.append([symbol, name, type, cond, tf, val, len1, len2, msg, isPaused])

            self.model = ListModel(data)    
            self.ui.lsvMyAlerts.setModel(self.model) 

            cursor.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            con.close()
