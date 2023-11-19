from PySide6.QtWidgets import QDialog

import sys
import json
import mysql.connector
from mysql.connector import errorcode

from UIFiles.ui_alertDialog import Ui_dlgAlert
from APIMethods import getQuote2, getQuote

class AlertDlg(QDialog):
    def __init__(self, stkSym, stkName, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgAlert()
        self.ui.setupUi(self)

        self.stkSymbol = stkSym
        self.stkName = stkName

        # self.dlgAlert = dlgAlert #pointer to alert window stored. To close it when user a set alert successfully.

        self.addConnectors()

        self.ui.dsbAlertVal.setMaximum(sys.float_info.max)
        self.ui.leStkName.setText(self.stkName)
        print(self.ui.leStkName.text())
        self.ui.leStkName.setReadOnly(True) 

        stk = json.loads(getQuote2("shubh", self.stkName, 'tc', 'NSE'))
        self.ui.dsbAlertVal.setValue(stk['data']['last_price'])

        self.ui.lblTimeFrame.hide()
        self.ui.cmbTimeFrame.hide()
        self.ui.lblLen1.hide()
        self.ui.lblLen2.hide()
        self.ui.sbLen1.hide()
        self.ui.sbLen2.hide()
    
    def addConnectors(self):
        self.ui.btnSetAlert.clicked.connect(self.addAlert) #to set alert
        self.ui.cmbAlertCond.currentTextChanged.connect(self.validateCondition)
        self.ui.cmbAlertType.currentTextChanged.connect(self.validateType)

    def validateType(self):
        alertType = self.ui.cmbAlertType.currentText()
        if alertType == 'Price' or alertType == 'MA':
            self.ui.cmbAlertCond.clear()
            self.ui.cmbAlertCond.addItem('Greater Than')
            self.ui.cmbAlertCond.addItem('Less Than')
            
            self.ui.lblAlertVal.setVisible(True)
            self.ui.dsbAlertVal.setVisible(True)

            if(alertType == 'MA'):
                self.ui.lblTimeFrame.setVisible(True)
                self.ui.cmbTimeFrame.setVisible(True)

                self.ui.lblLen1.setVisible(True)
                self.ui.sbLen1.setVisible(True)
            else:
                self.ui.lblTimeFrame.hide()
                self.ui.cmbTimeFrame.hide()

                self.ui.lblLen1.hide()
                self.ui.sbLen1.hide()

            self.ui.lblLen2.hide()
            self.ui.sbLen2.hide()
        elif alertType == 'Price + EMA' or alertType == 'Price + HMA':
            self.ui.cmbAlertCond.clear()
            self.ui.cmbAlertCond.ui.addItem('Greater Than')
            self.ui.cmbAlertCond.addItem('Less Than')
            self.ui.cmbAlertCond.addItem('Crossing Up')
            self.ui.cmbAlertCond.addItem('Crossing Down')
            self.ui.cmbAlertCond.addItem('In Between')
            self.ui.cmbAlertCond.addItem('Price > PrevMonthHigh')
            self.ui.cmbAlertCond.addItem('Price < PrevMonthLow')
            
            self.ui.lblTimeFrame.setVisible(True)
            self.ui.cmbTimeFrame.setVisible(True)

            self.ui.lblLen1.setVisible(True)  
            self.ui.sbLen1.setVisible(True)

            self.ui.lblLen2.hide()
            self.ui.sbLen2.hide()
    
    def validateCondition(self):
        alertType = self.ui.cmbAlertType.currentText()
        cond = self.ui.cmbAlertCond.currentText()
        if cond == 'In Between':
            self.ui.lblLen1.setVisible(True)
            self.ui.lblLen2.setVisible(True)

            self.ui.sbLen1.setVisible(True)
            self.ui.sbLen2.setVisible(True)
        else:
            self.ui.lblLen2.hide()
            self.ui.sbLen2.hide() 

        if(cond == 'Greater Than' or cond == 'Less Than'):
            if(alertType == 'Price + EMA' or alertType == 'Price + HMA'):
                self.ui.lblAlertVal.setVisible(True)  
                self.ui.dsbAlertVal.setVisible(True)  
        else:
            self.ui.lblAlertVal.hide()
            self.ui.dsbAlertVal.hide()
            
        stk = json.loads(getQuote2("shubh", self.stkName, 'tc', 'NSE'))
        self.ui.dsbAlertVal.setValue(stk['data']['last_price'])

    def addAlert(self):
        alertType = self.ui.cmbAlertType.currentText()
        alertCond = self.ui.cmbAlertCond.currentText()
        timeFrame = self.ui.cmbTimeFrame.currentText()
        alertVal = self.ui.dsbAlertVal.value()  
        len1 = self.ui.sbLen1.value() 
        len2 = self.ui.sbLen2.value() 
        alertMsg = self.ui.txteMsg.toPlainText()   

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""insert into alerts values('{self.stkSymbol}', '{self.stkName}', '{alertType}', '{alertCond}', '{timeFrame}', {alertVal}, {len1}, {len2}, '{alertMsg}') """
            print(query)
            cursor.execute(query)
            con.commit()

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

        print("alert added successfully")
        self.close()   #closes window when user successfully set alert
    