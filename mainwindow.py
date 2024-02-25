# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import  QThread
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py 

from UIFiles.ui_login import Ui_Login
from ProjectPages.messageDlg import MessageDlg
from ProjectPages.dashboardMW import Dashboard

import mysql.connector
from mysql.connector import errorcode

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle('Login')

        self.addConnectors()
    
    def addConnectors(self):
        self.ui.btnLogin.clicked.connect(self.login)

    def validateUser(self, uName, password):
        userPass = None
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select userPass from customer_details where userId = '{uName}'"""
            cursor.execute(query)
            for (uPass, ) in cursor:
                userPass = uPass

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

        if(userPass == None ):
            self.showMessage('Invalid UserName')
            return False

        if password != userPass:
            self.showMessage('Wrong Password')
            return False
        
        return True

    def showDashboard(self, userName):
        self.dashboard = Dashboard(userName)
        self.dashboard.show()

    def login(self):
        userName = self.ui.leUserName.text()
        password = self.ui.lePassword.text()

        if(self.validateUser(userName, password)):
            self.close()
            self.showDashboard(userName)

    def showMessage(self, msg):
        self.msgDlg = MessageDlg(msg)
        self.msgDlg.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())