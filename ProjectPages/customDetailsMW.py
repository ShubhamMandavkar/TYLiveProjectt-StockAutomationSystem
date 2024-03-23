
from PySide6.QtWidgets import QMainWindow

from ProjectPages.messageDlg import MessageDlg
from UIFiles.ui_customDetails import Ui_customDetails

import mysql.connector
from mysql.connector import errorcode

class UserDetails:
    def __init__(self, userName):
        self.userName = userName
        self.apiKey = ''
        self.apiSecretKey = ''
        self.profitThreshold = 100000
        self.averageThreshold = 100000
        self.deskNoti = True
        self.teleNoti = True
    
    def getUserDetails(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select apiKey, apiSecretKey, profitThreshold, averageThreshold, deskNoti, teleNoti from customer_details where userId = '{self.userName}'"""
            cursor.execute(query)
            for (key, sKey, profitThld, averageThld, deskNoti, teleNoti) in cursor:
                self.apiKey = key
                self.apiSecretKey = sKey 
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

class CustomDetails(QMainWindow):
    def __init__(self, userName, parent=None):
        super().__init__(parent)
        self.ui = Ui_customDetails()
        self.ui.setupUi(self)
        self.setWindowTitle('Custom Details')

        self.userDetails = UserDetails(userName)
        self.userDetails.getUserDetails()

        self.addConnector()
        self.setCstmDetails()

    def addConnector(self):
        self.ui.btnSave.clicked.connect(self.updateCstmDetails)

    def setCstmDetails(self):
        self.ui.leApiKey.setText(self.userDetails.apiKey)
        self.ui.leApiSecretKey.setText(self.userDetails.apiSecretKey)
        self.ui.dsbProfitThrld.setValue(self.userDetails.profitThreshold)
        self.ui.dsbAverageThrld.setValue(self.userDetails.averageThreshold)
        self.ui.cbDesktopNoti.setChecked(self.userDetails.deskNoti)
        self.ui.cbTelegramNoti.setChecked(self.userDetails.teleNoti)
        
        
    def updateCstmDetails(self):
        apiKey = self.ui.leApiKey.text()
        apiSecretKey = self.ui.leApiSecretKey.text()
        profitTh = self.ui.dsbProfitThrld.value()
        averageTh = self.ui.dsbAverageThrld.value()
        deskNoti = int(self.ui.cbDesktopNoti.isChecked())
        teleNoti = int(self.ui.cbTelegramNoti.isChecked())


        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()
            query = f"""UPDATE customer_details SET apiKey = '{apiKey}', apiSecretKey = '{apiSecretKey}',    profitThreshold = {profitTh}, averageThreshold = {averageTh}, deskNoti = {deskNoti}, teleNoti = {teleNoti} WHERE userId = '{self.userDetails.userName}'"""

            print(query)
            cursor.execute(query)
            con.commit()
            print(cursor.rowcount, " row updated")
            self.showMessage('Data updated successfully...')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()

    def showMessage(self, msg):
        self.msgDlg = MessageDlg(msg)
        self.msgDlg.show()
