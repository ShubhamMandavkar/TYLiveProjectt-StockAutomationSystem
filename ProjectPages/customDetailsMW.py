
from PySide6.QtWidgets import QMainWindow

import mysql.connector
from mysql.connector import errorcode
from UIFiles.ui_customDetails import Ui_customDetails

class CustomDetails(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_customDetails()
        self.ui.setupUi(self)
        self.setWindowTitle('Custom Details')

        self.addConnector()
        self.loadCstmDetails()

    def addConnector(self):
        self.ui.btnSave.clicked.connect(self.updateCstmDetails)

    def loadCstmDetails(self):
        print("loaded custm_details")
        con = None
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()
            query = f"""select apiKey, apiSecretKey, profitThreshold, quantity, deskNoti, teleNoti from customer_details WHERE userId = 'shubh'"""

            cursor.execute(query)
            for (apiKey, apiSecretKey, profitThreshold, quantity, deskNoti, teleNoti) in cursor:
                self.ui.leApiKey.setText(apiKey)
                self.ui.leApiSecretKey.setText(apiSecretKey)
                self.ui.dsbProfitThrld.setValue(profitThreshold)
                self.ui.sbQuantity.setValue(quantity)
                self.ui.cbDesktopNoti.setChecked(deskNoti)
                self.ui.cbTelegramNoti.setChecked(teleNoti)
                    
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        else:
            con.close()

    def updateCstmDetails(self):
            apiKey = self.ui.leApiKey.text()
            apiSecretKey = self.ui.leApiSecretKey.text()
            profitTh = self.ui.dsbProfitThrld.value()
            quantity = self.ui.sbQuantity.value()

            deskNoti = int(self.ui.cbDesktopNoti.isChecked())
            teleNoti = int(self.ui.cbTelegramNoti.isChecked())


            try:
                con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
                cursor = con.cursor()
                query = f"""UPDATE customer_details SET apiKey = '{apiKey}', apiSecretKey = '{apiSecretKey}',    profitThreshold = {profitTh}, quantity = {quantity}, deskNoti = {deskNoti}, teleNoti = {teleNoti} WHERE userId = 'shubh'"""

                print(query)
                cursor.execute(query)
                con.commit()
                print(cursor.rowcount, " row updated")

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print("error:",err)
            else:
                con.close()


