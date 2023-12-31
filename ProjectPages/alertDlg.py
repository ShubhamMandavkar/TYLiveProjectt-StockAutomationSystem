from PySide6.QtWidgets import QDialog

import sys
import json
import mysql.connector
from mysql.connector import errorcode

from UIFiles.ui_alertDialog import Ui_dlgAlert
from APIMethods import getQuote2, getQuote, getQuoteFromYfinance
from workers import AlertWorker

class AlertDlg(QDialog):
    def __init__(self, stkSym, stkName, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgAlert()
        self.ui.setupUi(self)

        self.stkSymbol = stkSym
        self.stkName = stkName

        self.addConnectors()

        self.ui.dsbAlertVal.setMaximum(sys.float_info.max)
        self.ui.leStkName.setText(self.stkName)
        self.ui.leStkName.setReadOnly(True) 

        self.validateType() #by default type is set to price
        self.generateMsg()
    
    def addConnectors(self):
        self.ui.btnSetAlert.clicked.connect(self.addAlert) #to set alert
        self.ui.cmbAlertCond.currentTextChanged.connect(self.validateCondition)
        self.ui.cmbAlertCond.currentTextChanged.connect(self.generateMsg)

        self.ui.cmbAlertType.currentTextChanged.connect(self.validateType)
        self.ui.cmbAlertType.currentTextChanged.connect(self.generateMsg)

        self.ui.dsbAlertVal.valueChanged.connect(self.generateMsg)
        self.ui.cmbTimeFrame.currentTextChanged.connect(self.generateMsg)
        self.ui.sbLen1.valueChanged.connect(self.generateMsg)
        self.ui.sbLen2.valueChanged.connect(self.generateMsg)

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

                self.ui.lblAlertVal.hide()
                self.ui.dsbAlertVal.hide()
            else:
                self.ui.lblTimeFrame.hide()
                self.ui.cmbTimeFrame.hide()

                self.ui.lblLen1.hide()
                self.ui.sbLen1.hide()

            self.ui.lblLen2.hide()
            self.ui.sbLen2.hide()
        elif alertType == 'Price + EMA' or alertType == 'Price + HMA':
            self.ui.cmbAlertCond.clear()
            self.ui.cmbAlertCond.addItem('Greater Than')
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

            self.ui.lblAlertVal.hide()
            self.ui.dsbAlertVal.hide()

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

            query = f"""insert into alerts values('{self.stkSymbol}', '{self.stkName}', '{alertType}', '{alertCond}', '{timeFrame}', {alertVal}, {len1}, {len2}, '{alertMsg}', 0) """
            print(query)
            cursor.execute(query)
            con.commit()

            #add alert to alertlist in AlertWorker for processing
            AlertWorker.alertList.append({'stkSymbol' : self.stkSymbol, 'stkName' : self.stkName, 'alertType' : alertType, 'alertCond' : alertCond, 'timeFrame' : timeFrame, 'alertVal' : alertVal, 'len1' : len1, 'len2' : len2, 'alertMsg' : alertMsg, 'isPaused': 0})

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
    
    def generateMsg(self):
        alertType = self.ui.cmbAlertType.currentText()
        alertCond = self.ui.cmbAlertCond.currentText()
        tf = self.ui.cmbTimeFrame.currentText()
        price = self.ui.dsbAlertVal.value()

        if(alertType == 'Price'):
            self.alertMsg = '' + self.stkName + "''s price " + alertCond + ' ' + str(price)  
        elif(alertType == 'MA'):
            self.alertMsg = '' + self.stkName + "''s price " + alertCond + ' MA' +str(self.ui.sbLen1.value()) + ' on ' + tf + ' time frame' 
        elif(alertType == 'Price + EMA' or alertType == 'Price + HMA'):
            if alertType == 'Price + EMA':
                myMa = 'EMA'
            else:
                myMa = 'HMA'

            if(alertCond != 'In Between'):
                self.alertMsg = '' + self.stkName + "''s price " + alertCond + ' ' + myMa +str(self.ui.sbLen1.value())  + ' on ' + tf + ' time frame'
            else:
                self.alertMsg = '' + self.stkName + "''s price " + alertCond + ' ' + myMa +str(self.ui.sbLen1.value()) +' and ' + myMa +str(self.ui.sbLen2.value())  + ' on ' + tf + ' time frame'
        
        self.ui.txteMsg.setText(self.alertMsg)



