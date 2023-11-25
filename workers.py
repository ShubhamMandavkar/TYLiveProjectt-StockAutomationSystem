
from PySide6.QtCore import QObject, Signal

import mysql.connector
from mysql.connector import errorcode
from APIMethods import getQuote2, getQuote, getHoldings2
import json
import math
import time
import zroya
import talib
import numpy as np
import yfinance as yf
import pandas as pd
from algomojo.pyapi import *


class AlertWorker(QObject):
    sigDeletedAlert = Signal()
    isRunning = False
    alertList = []

    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    # noti.setAudio(audio=zroya.Audio.Alarm)
    
    tf = {'Daily' : '1d', 'Monthly' : '1mo', 'Weekly' : '1wk'}
    def getAlertList():
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "@Shubh2000", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select * from alerts"""
            cursor.execute(query)
            alerts = []
            for (sym, name, type, condition, tf, val, len1, len2, msg) in cursor:
                alert = dict()
                alert['stkSymbol'] = sym
                alert['stkName'] = name
                alert['alertType'] = type
                alert['alertCond'] = condition
                alert['timeFrame'] = tf
                alert['alertVal'] = val
                alert['len1'] = len1
                alert['len2'] = len2
                alert['alertMsg'] = msg

                alerts.append(alert)
            AlertWorker.alertList = alerts

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
    
    def calAverage(self, data, avgType, tf , avgLen = None):
        match avgType:
            case 'MA':
                Avg = talib.MA(data, timeperiod = avgLen)
                return Avg
            case 'Price + EMA':
                Avg = talib.EMA(data, timeperiod = avgLen)
                return Avg
            case 'Price + HMA':
                length = avgLen
                Avg = talib.WMA(2*talib.WMA(data, timeperiod = length/2)-talib.WMA(data, timeperiod = length), timeperiod = math.floor(math.sqrt(length)))
                return Avg


    def processAlerts(self):
        while(self.isRunning):
            for alert in AlertWorker.alertList:
                currPrice = json.loads(getQuote2('shubh',alert['stkSymbol'], 'tc', 'NSE'))['data']['close']
                match alert['alertCond']:
                    case 'Greater Than':
                        if alert['alertType'] == 'Price':
                            if currPrice > alert['alertVal']:
                                print(alert['stkName'], 'price is greater than ', alert['alertVal'])
                                self.noti.setFirstLine(alert['stkName']) 
                                self.noti.setSecondLine(str(str(alert['stkName']) + ' price is greater than ' + str(alert['alertVal'])))
                                zroya.show(self.noti)
                        elif alert['alertType'] == 'MA' or alert['alertType'] == 'Price + EMA' or alert['alertType'] == 'Price + HMA':
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                            Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                            if currPrice > Avg[-1]:
                                print(alert['stkName'], 'price is greater than EMA', alert['len1'])
                                self.noti.setFirstLine(alert['stkName']) 
                                self.noti.setSecondLine(str(str(alert['stkName']) + ' price is greater than EMA' + str(alert['len1'])))
                                zroya.show(self.noti)
                                
                    case 'Less Than':
                        if currPrice < alert['alertVal']:
                            print(alert['stkName'], 'price is less than ', alert['alertVal'])
                            self.noti.setFirstLine(alert['stkName']) 
                            self.noti.setSecondLine(str(str(alert['stkName']) + ' price is less than ' + str(alert['alertVal'])))
                            zroya.show(self.noti)
                        
                        elif alert['alertType'] == 'MA' or alert['alertType'] == 'Price + EMA' or alert['alertType'] == 'Price + HMA':
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                            Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                            if currPrice < Avg[-1]:
                                print(alert['stkName'], 'price is greater than EMA', alert['len1'])
                                self.noti.setFirstLine(alert['stkName']) 
                                self.noti.setSecondLine(str(str(alert['stkName']) + ' price is greater than EMA' + str(alert['len1'])))
                                zroya.show(self.noti)
                    case 'Crossing Up':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                        if((df['Open'][-1] < Avg[-1] or df['Close'][-2] < Avg[-2]) and df['Close'] > Avg[-1]):
                            print(alert['stkName'], 'crosses up the price ', alert['alertVal'])
                            self.noti.setFirstLine(alert['stkName']) 
                            self.noti.setSecondLine(str(str(alert['stkName']) + ' crosses up the price ' + str(alert['alertVal'])))
                            zroya.show(self.noti)                            
                    case 'Crossing Down':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['len1']])

                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len1'])

                        if((df['Open'][-1] > Avg[-1] or df['Close'][-2] > Avg[-2]) and df['Close'] < Avg[-1]):
                            print(alert['stkName'], 'crosses up the price ', alert['alertVal'])
                            self.noti.setFirstLine(alert['stkName']) 
                            self.noti.setSecondLine(str(str(alert['stkName']) + ' crosses up the price ' + str(alert['alertVal'])))
                            zroya.show(self.noti)   
                        pass
                    case 'Price > PrevMonthHigh':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'], alert['len1'])

                        currMP = df['Close'][-1]
                        prevHigh = max(df['Close'][-2], df['Close'][-3])
                        if Avg[-1] > Avg[-2] and Avg[-2] > Avg[-3]: #uptrend
                            if currMP > prevHigh :
                                print(alert['stkName'], 'Breaks the previous month high of')
                                self.noti.setFirstLine(alert['stkName']) 
                                self.noti.setSecondLine(str(str(alert['stkName']) + ' Breaks the previous month high'))
                                zroya.show(self.noti)
                    case 'Price < PrevMonthLow':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                        
                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len1'])

                        currMP = df['Close'][-1]
                        prevLow = min(df['Close'][-2], df['Close'][-3])
                        if Avg[-1] < Avg[-2] and Avg[-2] < Avg[-3]: #downtrend
                            if currMP < prevLow :
                                print(alert['stkName'], 'Breaks the previous month low')
                                self.noti.setFirstLine(alert['stkName']) 
                                self.noti.setSecondLine(str(str(alert['stkName']) + ' Breaks the previous month low'))
                                zroya.show(self.noti)
                    case 'In Between':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                        #EMAs        
                        Avg1 = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len1'])
                        Avg2 = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len2'])
                        currMP = df['Close'][-1] 
                        if (currMP < Avg1[-1] and currMP > Avg2[-1]) or (currMP > Avg1[-1] and currMP < Avg2[-1]):
                            print('Price of ' , alert['stkName'], 'is in between', 'EMA'+str(alert['len1']), 'and', 'EMA'+str(alert['len2']))
                            self.noti.setFirstLine(alert['stkName']) 
                            self.noti.setSecondLine('Price of ' + str(alert['stkName']) + ' is in between ' + 'EMA'+ str(alert['len1']) + ' and ' + 'EMA'+str(alert['len2']))
                            zroya.show(self.noti)

            time.sleep(5)
            # self.getAlertList()
            print("processAlerts Called")
    
    

class HoldingsWorker(QObject):
    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    # noti.setAudio(audio=zroya.Audio.Alarm)

    isRunning = True
    holdings = json.dumps({ "status": "success", "data": []})   #static variable to share holdings for all objects

    sigChngHoldData = Signal(pd.DataFrame)   #signals to communicate with other threads
    sigNoHoldData = Signal()

    def __init__(self, key='', sKey='', brCode='tc'):
        super().__init__()
        self.apiKey = key
        self.apiSecretKey = sKey
        self.brCode = brCode
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)

        #to show holdings in holdings page
        self.isHoldingsPage = False
        
    
    def fetchHoldings(self, brCode = 'tc'):
        while(HoldingsWorker.isRunning):
            # HoldingsWorker.holdings = json.loads(json.dumps(self.algomojo.Holdings(broker=brCode)))
            # HoldingsWorker.holdings = self.algomojo.Holdings(broker=brCode) #use above if this not work
            HoldingsWorker.holdings = getHoldings2() #testing purpose only

            time.sleep(5)

    def myAction(nId, actionId):
        if(actionId == 0):
            print("stock sold successfully")
        elif(actionId == 1):
            print("Thank you for response")

    def processHoldings(self):
        while(HoldingsWorker.isRunning):
            myData = json.loads(HoldingsWorker.holdings)

            if(len(myData['data']) != 0):
                for holding in myData['data']:
                    if(holding['PL'] > 15):
                        print('Above 15% profit')
                        
                        self.noti.setFirstLine("Stock Profit Notification")
                        self.noti.setSecondLine(holding['symbol'] + "'s Stock profit above threshold!!!")
                        # self.noti.addAction("sell")
                        # self.noti.addAction("No")
                        # zroya.show(self.noti, on_action= self.myActio)
                        zroya.show(self.noti)

            time.sleep(5)
            print("Holding function ")                            

    def getHoldingsTableModel(self):
        while(self.isHoldingsPage):
            myData = json.loads(HoldingsWorker.holdings)
            
            if(len(myData['data']) != 0):
                dfHoldings = pd.DataFrame(myData['data'], columns=['symbol', 'holdqty','average_price','invest_val','hld_val','PL'])
                self.sigChngHoldData.emit(dfHoldings)
            else:
                self.sigNoHoldData.emit()
 
            time.sleep(5)
            print("Holding function ")

class WatchlistWorker(QObject):
    isRunning = False
    isWLChanged = False
    watchlistData = pd.DataFrame({})

    sigChngWLData = Signal(list)

    def getWatchlistTableModel(self):
        while(self.isRunning):
            data = []
            for i in self.watchlistData.index:
                stk = yf.Ticker(self.watchlistData['Symbol'][i]+".NS")
                hist = stk.history(period = '1d', interval = '1d')

                #item method is used to retrieve data only else it return data with index
                open =  round(hist['Open'].item(), 2)
                high =  round(hist['High'].item(), 2)
                low =  round(hist['Low'].item(), 2)
                close =  round(hist['Close'].item(), 2)
                data.append([self.watchlistData['Symbol'][i], self.watchlistData['Name'][i], open, high, low, close])

                if(self.isRunning == False or self.isWLChanged): # if watchlist is changed or watchlist page is closed stop execution
                    break
            
            if self.isWLChanged or not self.isRunning:
                    self.isWLChanged = False
                    continue

            self.sigChngWLData.emit(data)
            print('in watchlist worker')
            time.sleep(5)
    
    def setWatchlistChanged(self):
        self.isWLChanged = True