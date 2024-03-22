from datetime import datetime, timedelta
from PySide6.QtCore import QObject, Signal, QReadWriteLock

import mysql.connector
from mysql.connector import errorcode
from APIMethods import getHoldings2, getQuoteFromYfinance
import json
import math
import time
import zroya
import talib
import yfinance as yf
import pandas as pd
from algomojo.pyapi import *
from telethon import TelegramClient
from apiDetails import apiId, apiHashId
import asyncio
import requests

class TeleApiWorker(QObject):
    finished = Signal()
    teleClient = TelegramClient('MySession', apiId, apiHashId)
    loop = None
    def __init__(self, loop=None):
        super().__init__()
        TeleApiWorker.loop = loop
        
    def startEventLoop(self):
        asyncio.set_event_loop(self.loop)
        TeleApiWorker.loop.run_forever()
    
    async def sendMessage(msg):
        async with TeleApiWorker.teleClient as client:
            await client.send_message('me', msg)

def isNetworkConnected():
    try:
        response = requests.get("http://www.google.com")
        return True
    except requests.ConnectionError:
        return False
    except Exception:
        return False

class AlertWorker(QObject):
    sigDeletedAlert = Signal()
    sigShowBuyOrderWidget = Signal(str)
    sigShowSellOrderWidget = Signal()
    isRunning = False
    alertList = []

    #desktop notification setup
    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    noti.setAudio(audio=zroya.Audio.Alarm)
    noti.addAction("BUY")
    noti.addAction("SELL")
    
    tf = {'Daily' : '1d', 'Monthly' : '1mo', 'Weekly' : '1wk'}
    def __init__(self, desktopNoti, teleNoti):
        super().__init__()
        self.notiLock = QReadWriteLock()
        self.desktopNoti = desktopNoti
        self.teleNoti = teleNoti
    
    def changeDetails(self, desktopNoti, teleNoti):
        print('changeDetails called')
        print(desktopNoti, teleNoti)
        self.notiLock.lockForWrite()
        self.desktopNoti = desktopNoti
        self.teleNoti = teleNoti
        self.notiLock.unlock()

    def getAlertList():
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select * from alerts"""
            cursor.execute(query)
            alerts = []
            for (sym, name, type, condition, tf, val, len1, len2, msg, isPaused, lastTriggerTime) in cursor:
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
                alert['isPaused'] = isPaused
                alert['lastTriggerTime'] = lastTriggerTime

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

    def pauseAlert(self, alert):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #update the values of alert
            query = f"""update alerts set isPaused = 1 where stkSymbol = '{alert['stkSymbol']}' and alertType = '{alert['alertType']}' and alertCondition = '{alert['alertCond']}' and timeFrame = '{alert['timeFrame']}' and alertVal = {alert['alertVal']} and len1 = {alert['len1']} and len2 = {alert['len2']}"""
            cursor.execute(query)
            con.commit()
            print('alert paused')

            AlertWorker.getAlertList()
            #emit signal to change the myAlerts list

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            con.close()
    
    def setLastTriggerTime(self, alert, lastTriggerTime):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #update the values of alert
            query = f"""update alerts set prevTriggerTime = '{lastTriggerTime}' where stkSymbol = '{alert['stkSymbol']}' and alertType = '{alert['alertType']}' and alertCondition = '{alert['alertCond']}' and timeFrame = '{alert['timeFrame']}' and alertVal = {alert['alertVal']} and len1 = {alert['len1']} and len2 = {alert['len2']}"""
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
            con.close()
    
    def checkLastTriggerTime(self, alert): #check for the lastTriggerTime
        if(alert['lastTriggerTime']) == None:
            return True 

        lastTriggerTime = datetime.strptime(alert['lastTriggerTime'],'%Y-%m-%d %H:%M:%S.%f') 
        currTime = datetime.now() - timedelta(minutes=1)

        return lastTriggerTime < currTime
    
    def myAction(self, nId, actionId):  
        if(actionId == 0):
            self.sigShowBuyOrderWidget.emit(self.noti.getFirstLine())
            print("Thank you for response")
        elif(actionId == 1):
            self.sigShowSellOrderWidget.emit()
            print("Thank you for response")

    def sendNotiToDesktop(self, title, message):
        self.notiLock.lockForRead()
        if(self.desktopNoti):
            self.noti.setFirstLine(title) 
            self.noti.setSecondLine(message)
            zroya.show(self.noti, on_action= self.myAction) #notificatoin sent to desktop
            # zroya.show(self.noti) #notificatoin sent to desktop
        self.notiLock.unlock()

    def processAlerts(self):
        while(self.isRunning):
            for alert in AlertWorker.alertList:
                if(alert['isPaused']):
                    continue

                try:
                    # currPrice = json.loads(getQuote2('shubh',alert['stkSymbol'], 'tc', 'NSE'))['data']['close']
                    currPrice = getQuoteFromYfinance('shubh',alert['stkSymbol'], 'tc', 'NSE')['Close'].iloc[-1]
                except Exception as e:
                    print(e)
                    continue

                match alert['alertCond']:
                    case 'Greater Than':
                        if alert['alertType'] == 'Price':
                            if currPrice > alert['alertVal'] and self.checkLastTriggerTime(alert):
                                print(alert['stkName'], 'price is greater than ', alert['alertVal'])

                                title = alert['stkSymbol']
                                msg = str(str(alert['stkName']) + ' price is greater than ' + str(alert['alertVal']))
                                self.sendNotiToDesktop(title, msg)

                                self.notiLock.lockForRead()
                                if self.teleNoti :
                                    asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                self.notiLock.unlock()

                                alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database

                        elif alert['alertType'] == 'MA' or alert['alertType'] == 'Price + EMA' or alert['alertType'] == 'Price + HMA':
                            try:
                                stk = yf.Ticker(alert['stkSymbol']+".NS")
                                df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                                Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                                

                                if currPrice > Avg[-1] and self.checkLastTriggerTime(alert):
                                    alertType = ''
                                    if(alert['alertType'] == 'MA'):
                                        alertType = 'MA'
                                    elif(alert['alertType'] == 'Price + EMA'):
                                        alertType = 'EMA'
                                    elif(alert['alertType'] == 'Price + HMA'):
                                        alertType = 'HMA'

                                    print(alert['stkName'], 'price is greater than EMA', alert['len1'])

                                    title = alert['stkSymbol']
                                    msg = str(str(alert['stkName']) + ' price is greater than '+ alertType + str(alert['len1']))
                                    self.sendNotiToDesktop(title, msg)
                                
                                    self.notiLock.lockForRead()
                                    if self.teleNoti :
                                        asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                    self.notiLock.unlock()

                                    alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                    self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database
                            except Exception as e : 
                                print('Exception in Alertworker Less than')    
                    case 'Less Than':
                        if alert['alertType'] == 'Price':
                            if currPrice < alert['alertVal'] and self.checkLastTriggerTime(alert):
                                print(alert['stkName'], 'price is less than ', alert['alertVal'])

                                title = alert['stkSymbol']
                                msg = str(str(alert['stkName']) + ' price is less than ' + str(alert['alertVal']))
                                self.sendNotiToDesktop(title, msg)
                                
                                self.notiLock.lockForRead()
                                if self.teleNoti :
                                    asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                self.notiLock.unlock()
                                
                                alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database

                        elif alert['alertType'] == 'MA' or alert['alertType'] == 'Price + EMA' or alert['alertType'] == 'Price + HMA':
                            try :
                                stk = yf.Ticker(alert['stkSymbol']+".NS")
                                df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                                Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                                if currPrice < Avg[-1] and self.checkLastTriggerTime(alert):
                                    alertType = ''
                                    if(alert['alertType'] == 'MA'):
                                        alertType = 'MA'
                                    elif(alert['alertType'] == 'Price + EMA'):
                                        alertType = 'EMA'
                                    elif(alert['alertType'] == 'Price + HMA'):
                                        alertType = 'HMA'

                                    print(alert['stkName'], 'price is greater than EMA', alert['len1'])

                                    title = alert['stkSymbol']
                                    msg = str(str(alert['stkName']) + ' price is greater than ' + alertType + str(alert['len1']))
                                    self.sendNotiToDesktop(title, msg)
                                    
                                    self.notiLock.lockForRead()
                                    if self.teleNoti :
                                        asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                    self.notiLock.unlock()

                                    alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                    self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database
                            except Exception as e : 
                                print('Exception in Alertworker Less than')
                    case 'Crossing Up':
                        try:
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                            Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                            if((df['Open'].iloc[-1] < Avg[-1] or df['Close'].iloc[-2] < Avg[-2]) and df['Close'] > Avg[-1] and self.checkLastTriggerTime(alert)):
                                print(alert['stkName'], 'crosses up the price ', alert['alertVal'])

                                title = alert['stkSymbol']
                                msg = str(str(alert['stkName']) + ' crosses up the price ' + str(alert['alertVal']))
                                self.sendNotiToDesktop(title, msg)

                                self.notiLock.lockForRead()
                                if self.teleNoti :
                                    asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                self.notiLock.unlock()

                                alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database
                        except Exception as e : 
                            print('Exception in Alertworker crossing up')

                    case 'Crossing Down':
                        try:
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['len1']])

                            Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                    alert['timeFrame'],   alert['len1'])

                            if((df['Open'].iloc[-1] > Avg[-1] or df['Close'].iloc[-2] > Avg[-2]) and df['Close'] < Avg[-1] and self.checkLastTriggerTime(alert)):
                                print(alert['stkName'], 'crosses down the price ', alert['alertVal'])

                                title = alert['stkSymbol']
                                msg = str(str(alert['stkName']) + ' crosses down the price ' + str(alert['alertVal']))
                                self.sendNotiToDesktop(title, msg)

                                self.notiLock.lockForRead()
                                if self.teleNoti :
                                    asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                self.notiLock.unlock()

                                alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database
                        except Exception as e : 
                            print('Exception in Alertworker crossing down')
                                
                    case 'In Between':
                        try:
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                            #EMAs        
                            Avg1 = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                    alert['timeFrame'],   alert['len1'])
                            Avg2 = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                    alert['timeFrame'],   alert['len2'])
                            currMP = df['Close'].iloc[-1] 
                            if (currMP < Avg1[-1] and currMP > Avg2[-1]) or (currMP > Avg1[-1] and currMP < Avg2[-1]) and self.checkLastTriggerTime(alert):
                                print('Price of ' , alert['stkName'], 'is in between', 'EMA'+str(alert['len1']), 'and', 'EMA'+str(alert['len2']))

                                title = alert['stkSymbol']
                                msg = str('Price of ' + str(alert['stkName']) + ' is in between ' + 'EMA'+ str(alert['len1']) + ' and ' + 'EMA'+str(alert['len2']))
                                self.sendNotiToDesktop(title, msg)
                                
                                self.notiLock.lockForRead()
                                if self.teleNoti :
                                    asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                self.notiLock.unlock()

                                alert['lastTriggerTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string
                                self.setLastTriggerTime(alert, alert['lastTriggerTime']) #change in database
                        except Exception as e : 
                            print('Exception in Alertworker In Between')
            print("processAlerts Called")  
            time.sleep(5)

class HoldingsWorker(QObject):
    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    noti.setAudio(audio=zroya.Audio.Alarm)
    noti.addAction("BUY")
    noti.addAction("SELL")

    holdings = { "status": "success", "data": []}   #static variable to share holdings for all objects
    lastNotificationSentTime = pd.DataFrame()
    isRunning = True
    isNetConnected = True

    sigChngHoldData = Signal(pd.DataFrame)   #signals to communicate with other threads
    sigNoHoldData = Signal()
    sigHoldDetails = Signal(pd.DataFrame) #signal to emit holding details to be shown on home page
    sigShowMsg = Signal(str)
    finished = Signal() 

    def __init__(self, key='', sKey='', brCode='tc', profitTh = 100000, avgTh= 100000, desktopNoti = False, teleNoti = False):
        super().__init__()
        self.lock = QReadWriteLock()
        self.notiLock = QReadWriteLock()
        self.apiKey = key
        self.apiSecretKey = sKey
        self.profitThreshold = profitTh
        self.avgThreshold = avgTh
        self.brCode = brCode

        self.desktopNoti = desktopNoti #tells whether to send notification to desktop or not
        self.teleNoti = teleNoti

        self.investedValue = 0
        self.currentValue = 0
        self.profitAndLoss = 0
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)

        #to show holdings in holdings page
        self.isHoldingsPage = False

    def changeDetails(self, key='', sKey='', brCode = 'tc', profitTh = 100000, avgTh= 100000, desktopNoti = False, teleNoti = False):
        self.lock.lockForWrite()
        self.apiKey = key
        self.apiSecretKey = sKey
        self.brCode = brCode
        self.profitThreshold = profitTh
        self.avgThreshold = avgTh
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)
        self.lock.unlock()

        self.notiLock.lockForWrite()
        self.desktopNoti = desktopNoti 
        self.teleNoti = teleNoti
        self.notiLock.unlock()

    def tempFunction(self): #this function is useful for sending the notification at a specific interval
        self.lock.lockForRead()
        status = HoldingsWorker.holdings['status']
        self.lock.unlock()

        if(status == 'error'):
            return

        self.lock.lockForRead()
        tempHoldings = pd.DataFrame(pd.DataFrame(HoldingsWorker.holdings['data'])['symbol'])
        self.lock.unlock()

        tempHoldings['lastNotiSent'] = None
        tempHoldings.set_index('symbol', inplace= True)

        if(HoldingsWorker.lastNotificationSentTime.size == 0):
            HoldingsWorker.lastNotificationSentTime = tempHoldings
        else:
            #HoldingsWorker.lastNotificationSentTime contains symbols which are present in both and symbols which are only present in tempHoldings
            HoldingsWorker.lastNotificationSentTime = pd.concat([HoldingsWorker.lastNotificationSentTime[HoldingsWorker.lastNotificationSentTime.index.isin(tempHoldings.index) == True], tempHoldings[tempHoldings.index.isin(HoldingsWorker.lastNotificationSentTime.index) == False]])
            
    def checkLastNotiSend(self, stkSymbol):
        if(stkSymbol not in HoldingsWorker.lastNotificationSentTime.index):
            return False

        if(HoldingsWorker.lastNotificationSentTime.loc[stkSymbol, 'lastNotiSent']) == None:
            return True 

        lastTriggerTime = datetime.strptime(HoldingsWorker.lastNotificationSentTime.loc[stkSymbol, 'lastNotiSent'],'%Y-%m-%d %H:%M:%S.%f') 
        currTime = datetime.now() - timedelta(minutes=1)

        return lastTriggerTime < currTime

    def fetchHoldings(self):
        while(HoldingsWorker.isRunning):
            try :
                self.lock.lockForWrite()
                # HoldingsWorker.holdings = json.loads(json.dumps(self.algomojo.Holdings(broker=self.brCode)))
                
                # print(HoldingsWorker.holdings['status'])
                # print(HoldingsWorker.holdings['error_msg'])
                # print(HoldingsWorker.holdings['error_type'])

                # HoldingsWorker.holdings = self.algomojo.Holdings(broker=brCode) #use above if this not work
                HoldingsWorker.holdings = json.loads(getHoldings2()) #testing purpose only
                self.lock.unlock()

                self.tempFunction()

                HoldingsWorker.isNetConnected = True
            except requests.exceptions.ConnectionError:
                self.lock.unlock()
                HoldingsWorker.isNetConnected = False
            except Exception as e:
                print(e)
            

            print('HoldingsfetchingThread called')
            time.sleep(5)
        
        print('HoldingFetchingThred finished')

    def myAction(nId, actionId):
        if(actionId == 0):
            print("stock sold successfully")
        elif(actionId == 1):
            print("Thank you for response")

    def sendDeskNotification(self, title, msg):
        self.noti.setFirstLine(title)
        self.noti.setSecondLine(msg)
        zroya.show(self.noti, on_action= self.myAction)
        # zroya.show(self.noti)

    def processHoldings(self):
        while(HoldingsWorker.isRunning):
            self.lock.lockForRead()
            myData = HoldingsWorker.holdings
            self.lock.unlock()

            tempInvestedValue = 0
            tempCurrentValue = 0
            tempProfitAndLoss = 0
            
            if(myData['status'] == 'success'):
                for holding in myData['data']:
                    tempInvestedValue += holding['invest_val']
                    tempCurrentValue += holding['hld_val']
                    tempProfitAndLoss += holding['PL']

                    #code to check for pofit booking
                    if(((holding['invest_val']+(holding['invest_val'] * self.profitThreshold)/100) <= holding['hld_val']) and self.checkLastNotiSend(holding['symbol'])):
                        print('Above given% profit')
                        
                        self.notiLock.lockForRead()
                        if(self.desktopNoti):
                            self.sendDeskNotification("Stock Profit Notification", holding['symbol'] + "'s Stock profit above " + str(self.profitThreshold) + "% threshold!!!")


                            HoldingsWorker.lastNotificationSentTime.loc[holding['symbol'], 'lastNotiSent'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string

                        if self.teleNoti :
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(str(holding['symbol'] + "'s Stock profit above " + str(self.profitThreshold) + "% threshold!!!")), TeleApiWorker.loop)
                        self.notiLock.unlock()


                    #code to check for average
                    if(holding['ltp'] < holding['average_price'] - (holding['average_price']*(self.avgThreshold*0.01)) and self.checkLastNotiSend(holding['symbol'])):
                        print('Average', holding['symbol'],'stock ?')
                        self.notiLock.lockForRead()
                        if(self.desktopNoti):
                            self.sendDeskNotification("Stock Averaging Notification", holding['symbol'] + "'s Stock price 5% below average price!!!")

                            HoldingsWorker.lastNotificationSentTime.loc[holding['symbol'], 'lastNotiSent'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') #converting datetime to string

                        if self.teleNoti :
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(str(holding['symbol'] + "'s Stock price 5% below average price!!!")), TeleApiWorker.loop)
                        self.notiLock.unlock()

            
            self.investedValue = tempInvestedValue
            self.currentValue = tempCurrentValue
            self.profitAndLoss = tempProfitAndLoss

            self.sigHoldDetails.emit( pd.DataFrame({'investedValue': [self.investedValue], 'currentValue': [self.currentValue], 'profitAndLoss': [self.profitAndLoss]}) )

            time.sleep(5)
            print("process Holdings called")                            

    def roundDigit(self, val):
        return round(val, 2)

    def getHoldingsTableModel(self):
        isApiInvalidMsgShown = False 
        isNetNotConnectedMsgSend = False
        
        while(self.isHoldingsPage):
            if(not HoldingsWorker.isNetConnected): #if network is not connected
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')
                    isNetNotConnectedMsgSend = True
                continue

            self.lock.lockForRead()
            if(HoldingsWorker.holdings['status'] == 'success'):
                if(len(HoldingsWorker.holdings['data']) != 0):
                    self.dfHoldings = pd.DataFrame(HoldingsWorker.holdings['data'], columns=['symbol', 'ltp', 'holdqty','average_price','invest_val','hld_val','PL'])

                    self.dfHoldings['ltp'] = self.dfHoldings['ltp'].apply(self.roundDigit) 
                    self.dfHoldings['average_price'] = self.dfHoldings['average_price'].apply(self.roundDigit) 
                    self.dfHoldings['invest_val'] = self.dfHoldings['invest_val'].apply(self.roundDigit) 
                    self.dfHoldings['hld_val'] = self.dfHoldings['hld_val'].apply(self.roundDigit) 
                    self.dfHoldings['PL'] = self.dfHoldings['PL'].apply(self.roundDigit) 
                    self.sigChngHoldData.emit(self.dfHoldings)
                else:
                    self.sigNoHoldData.emit()
                
                isApiInvalidMsgShown = False
            else:
                if(not isApiInvalidMsgShown):
                    #show message
                    self.sigShowMsg.emit(HoldingsWorker.holdings['error_msg'])
                    self.sigNoHoldData.emit()
                    isApiInvalidMsgShown = True

            self.lock.unlock()
            isNetNotConnectedMsgSend = False

            time.sleep(5)
            print("getHoldingTbleModel function ")

        print('getHoldingTbleModel finished')
        self.finished.emit()

class WatchlistWorker(QObject):
    sigShowWLData = Signal(pd.DataFrame)   #signals to communicate with other threads
    sigShowMsg = Signal(str)
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.isRunning = True
        self.isWLChanged = False
        self.stkList = {}
        self.currWL = None
        self.lock = QReadWriteLock() #lock to synchronize the use of shared resource between threads

    def getWLSymbols(self, watchlist):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
            cursor = con.cursor()
            query = f"""select * from {watchlist}"""
            cursor.execute(query)

            self.lock.lockForWrite()
            for stkSym, stkName in cursor:
                self.stkList[stkSym] = stkName
            self.lock.unlock()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            con.close()

    def addSymbolToWL(self, stkSym, stkName):
        self.lock.lockForWrite()
        self.stkList[stkSym] = stkName #add stock in worker list
        self.lock.unlock()

    def deleteSymbolFromWL(self, stkSym):
        self.lock.lockForWrite()
        try:
            self.stkList.pop(stkSym)
        except Exception as e:
            print(e)
        self.lock.unlock()

    def clearWL(self):
        self.lock.lockForWrite()
        self.stkList.clear()  #clear stocks list of previous watchlist
        self.lock.unlock()

    def fetchWLData(self):            
        self.lock.lockForRead()
        i = 0
        while(i < len(self.stkList.keys())):
            if(not isNetworkConnected()): #if network is not connected stop the operation
                break

            if(self.isRunning == False or self.isWLChanged): #watchlist closed or watchlist changed
                break
            
            key = list(self.stkList.keys())[i]
            name = self.stkList[key]

            # importing data from yfinance
            try:
                hist = yf.download(key + '.NS', period='1d', interval='1d', progress= False)

                # #item method is used to retrieve data only else it return data with index
                open =  round(hist['Open'].item(), 2)
                high =  round(hist['High'].item(), 2)
                low =  round(hist['Low'].item(), 2)
                close =  round(hist['Close'].item(), 2)

                self.lock.unlock()
                time.sleep(0.1)
                self.lock.lockForRead()

                if(key in self.stkList.keys()):
                    self.sigShowWLData.emit(pd.DataFrame({'Symbol' : [key], 'Name' : [name], 'Open' : [open], 'High' : [high], 'Low' : [low], 'Close' : [close]}))

            except Exception as e:
                print('Exception in watchlist thread', e)

            i = i + 1

        self.lock.unlock()
    
    def updateWL(self):
        isNetNotConnectedMsgSend = False
        while(self.isRunning):
        # for i in range(3):
            if(isNetworkConnected()):
                self.fetchWLData()

            if(isNetworkConnected()):
                isNetNotConnectedMsgSend = False
            else:
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')
                    isNetNotConnectedMsgSend = True

            if(self.isRunning == False): #watchlist closed
                continue
            
            if(self.isWLChanged): #if watchlist changed
                self.clearWL()
                self.getWLSymbols(self.currWL)
                self.isWLChanged = False
                continue

            time.sleep(5)

            print('update WL called')
        print('--------------watchlist thread ended--------------')
        self.finished.emit()
    
    def setWatchlistChanged(self, wlName):
        self.isWLChanged  = True
        self.currWL = wlName

class StockWorker(QObject):
    sigShowStkDetails = Signal(pd.DataFrame)
    sigShowMsg = Signal(str)
    finished = Signal()

    def __init__(self, name):
        super().__init__()
        self.stkSymbol = name
        self.isRunning = True

    def fetchStockDetails(self):
        isNetNotConnectedMsgSend = False

        while(self.isRunning):
            try:
                stkDf = yf.download(self.stkSymbol + '.NS', period='1d', interval='1d', progress= False)
                stk = yf.Ticker(self.stkSymbol + '.NS')
                stkInfo = stk.info  #causing crash in offline mode when closing stockDetails page
                if not stkDf.empty :
                    self.sigShowStkDetails.emit(pd.DataFrame({'Open': stkDf['Open'], 
                                                        'High': stkDf['High'], 
                                                        'Low': stkDf['Low'], 
                                                        'Close': stkDf['Close'], 
                                                        'Volume': stkDf['Volume'], 
                                                        'fiftyTwoWeekHigh': stkInfo['fiftyTwoWeekHigh'], 
                                                        # 'fiftyTwoWeekHigh': 500, 
                                                        'fiftyTwoWeekLow': stkInfo['fiftyTwoWeekLow'] 
                                                        # 'fiftyTwoWeekLow': 400 
                                                        }))
                    
                isNetNotConnectedMsgSend = False    
            except requests.exceptions.ConnectionError:
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')   
                    isNetNotConnectedMsgSend = True                                 
            except Exception as e:
                print('Exception in stkDetailsWorker', e)

            time.sleep(5)

        print('fetchStockDetails thread ended')
        self.finished.emit()

class SpecialAlertsWorker(QObject):
    sigSpecialAlerts = Signal(pd.DataFrame) #signal to emit specialAlerts satisfying stocks list
    sigShowMsg = Signal(str)
    finished = Signal()

    stkSymbolsList = pd.DataFrame({'stkSymbol': [], 
                                    'PMHTriggerTime': [], 'PMLTriggerTime': [],                             
                                    'PWHTriggerTime': [], 'PWLTriggerTime': []})
    stkSymbolsList.set_index('stkSymbol')

    alertsTriggeredList = pd.DataFrame({'stkSymbol': [], 
                                    'PMHTriggerTime': [], 'PMLTriggerTime': [],                             
                                    'PWHTriggerTime': [], 'PWLTriggerTime': []})
    alertsTriggeredList.set_index('stkSymbol')

    #desktop notification setup
    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    noti.setAudio(audio=zroya.Audio.Alarm)
    noti.addAction("BUY")
    noti.addAction("SELL")

    def __init__(self, desktopNoti = False, teleNoti = False):
        super().__init__()
        self.isRunning = True
        self.isSpecialAlertsPage = False
        self.lock = QReadWriteLock() #lock to synchronize the use of shared resource between threads

        self.notiLock = QReadWriteLock()
        self.desktopNoti = desktopNoti
        self.teleNoti = teleNoti
    
    def changeDetails(self, desktopNoti, teleNoti):
        self.notiLock.lockForWrite()
        self.desktopNoti = desktopNoti
        self.teleNoti = teleNoti
        self.notiLock.unlock()

    #get the list of symbols
    def getStkSymbolsList(self):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select stkSymbol, PMHTriggerTime, PMLTriggerTime, PWHTriggerTime, PWLTriggerTime from special_alerts_stk_list"""
            cursor.execute(query)
            stkList = {'stkSymbol': [], 'PMHTriggerTime': [], 'PMLTriggerTime': [], 'PWHTriggerTime': [], 'PWLTriggerTime': []}
            for (stkSymbol, PMHTriggerTime,  PMLTriggerTime,  PWHTriggerTime,  PWLTriggerTime) in cursor:
                stkList['stkSymbol'].append(stkSymbol)
                stkList['PMHTriggerTime'].append(PMHTriggerTime)
                stkList['PMLTriggerTime'].append(PMLTriggerTime)
                stkList['PWHTriggerTime'].append(PWHTriggerTime)
                stkList['PWLTriggerTime'].append(PWLTriggerTime)
                

            stkList = pd.DataFrame(stkList, columns=stkList.keys())
            stkList.set_index('stkSymbol', inplace= True)
            stkList.fillna('', inplace=True)

            self.lock.lockForWrite()
            SpecialAlertsWorker.stkSymbolsList = stkList
            self.lock.unlock()

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
    
    def addToSymbolsList(self, symbol):
        temp = pd.DataFrame({'stkSymbol': [symbol]})
        temp['PMHTriggerTime'] = '' 
        temp['PMLTriggerTime'] = ''
        temp['PWHTriggerTime'] = ''
        temp['PWLTriggerTime'] = ''

        temp.set_index('stkSymbol', inplace=True)
        
        self.lock.lockForWrite()
        SpecialAlertsWorker.stkSymbolsList = pd.concat([SpecialAlertsWorker.stkSymbolsList, temp])
        self.lock.unlock()

    def deleteFromSymbolsList(self, symbol):
        self.lock.lockForWrite()
        print(SpecialAlertsWorker.stkSymbolsList)
        SpecialAlertsWorker.stkSymbolsList.drop(symbol, inplace=True, axis=0)
        print(SpecialAlertsWorker.stkSymbolsList)
        self.lock.unlock()

    def clearSymbolsList(self):
        self.lock.lockForWrite()
        SpecialAlertsWorker.stkSymbolsList =  pd.DataFrame({'stkSymbol': [], 
                                                    'PMHTriggerTime': [], 'PMLTriggerTime': [],                             
                                                    'PWHTriggerTime': [], 'PWLTriggerTime': []})
        self.lock.unlock()

    def myAction(self, nId, actionId):  
        if(actionId == 0):
            self.sigShowBuyOrderWidget.emit(self.noti.getFirstLine())
            print("Thank you for response")
        elif(actionId == 1):
            self.sigShowSellOrderWidget.emit()
            print("Thank you for response")
    
    def sendNotiToDesktop(self, title, message):
        self.notiLock.lockForRead()
        if(self.desktopNoti):
            self.noti.setFirstLine(title) 
            self.noti.setSecondLine(message)
            zroya.show(self.noti, on_action= self.myAction) #notificatoin sent to desktop
        self.notiLock.unlock()

    def calAverage(self, data, avgType, avgLen = None):
        match avgType:
            case 'MA':
                Avg = talib.MA(data, timeperiod = avgLen)
                return Avg
            case 'EMA':
                Avg = talib.EMA(data, timeperiod = avgLen)
                return Avg
            case 'HMA':
                length = avgLen
                Avg = talib.WMA(2*talib.WMA(data, timeperiod = length/2)-talib.WMA(data, timeperiod = length), timeperiod = math.floor(math.sqrt(length)))
                return Avg

    def isNetworkConnected(self):
        try:
            response = requests.get("http://www.google.com")
            return True
        except requests.ConnectionError:
            return False
        except Exception:
            return False

    def setLastTriggerTime(self, symbol, type, lastTriggerTime):
        self.lock.lockForWrite()
        SpecialAlertsWorker.stkSymbolsList[type].loc[symbol] = lastTriggerTime
        self.lock.unlock()

        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""update special_alerts_stk_list set {type} = '{lastTriggerTime}' where stkSymbol = '{symbol}'"""
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
    
    def checkLastTriggerTime(self, symbol, type): #check for the lastTriggerTime
        ''' 
            function: checks the last trigger time 
            output : returns true if lastTriggerTime is more than 1 minute else false
        '''
        try:
            self.lock.lockForRead()
            lastTriggerTime = SpecialAlertsWorker.stkSymbolsList[type].loc[symbol]
            self.lock.unlock()

            if(lastTriggerTime == '') :
                return True 

            self.lock.lockForRead()
            lastTriggerTime = datetime.strptime(SpecialAlertsWorker.stkSymbolsList[type].loc[symbol], '%Y-%m-%d %H:%M:%S.%f') 
            self.lock.unlock()

            today = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0, 0, 0, 0)
            return lastTriggerTime < today #if lastTriggerTime is less than today

        except Exception as e:
            print(e)

        return False

    def isPriceCrossingPMH(self, symbol):
        '''checks if price is greater than previous month high'''
        try:
            monthDf = yf.download(symbol + ".NS", period="max", interval = '1mo', progress= False)
            dailyDf = yf.download(symbol + ".NS", period = '2d', interval = '1d', progress= False)

            Avg = self.calAverage(monthDf['Close'].to_numpy(), 'EMA', 50)
            currMP = monthDf['Close'].iloc[-1]

            if(monthDf.size >= 2):
                prevMonthHigh = monthDf['High'].iloc[-2]
                
                if Avg[-1] > Avg[-2] and Avg[-2] > Avg[-3]:
                    if(dailyDf['Open'].iloc[-1]<= prevMonthHigh or dailyDf['Close'].iloc[-2] <= prevMonthHigh) and currMP > prevMonthHigh:
                        return True
                    
                return False
            else:
                #the symbol has been listed in current month
                return True
        except Exception as e:
            print(e)

        return False

    def isPriceLowerThanPML(self, symbol):
        '''checks if price is lower than previous month low'''

        try:
            monthDf = yf.download(symbol + ".NS", period="max", interval = '1mo', progress= False)
            dailyDf = yf.download(symbol + ".NS", period = '2d', interval = '1d', progress= False)

            Avg = self.calAverage(monthDf['Close'].to_numpy(), 'EMA', 50)
            currMP = monthDf['Close'].iloc[-1]

            if(monthDf.size >= 2):
                prevMonthLow = monthDf['Low'].iloc[-2]
                
                if Avg[-1] < Avg[-2] and Avg[-2] < Avg[-3]:
                    if (dailyDf['Open'].iloc[-1] >= prevMonthLow or dailyDf['Close'].iloc[-2] >= prevMonthLow) and currMP < prevMonthLow:
                        return True
                    
                return False
            else:
                #the symbol has been listed in current month
                return True
        except Exception as e:
            print(e)

        return False

    def isPriceGreaterThanPWH(self, symbol):
        '''checks if price is greater than previous week high'''

        try:
            weekDf = yf.download(symbol + ".NS", period="1mo", interval = '1wk', progress= False)
            dailyDf = yf.download(symbol + ".NS", period = '2d', interval = '1d', progress= False)

            currMP = dailyDf['Close'].iloc[-1]

            if(weekDf.size >= 2):
                prevWeekHigh = weekDf['High'].iloc[-2]

                if (dailyDf['Open'].iloc[-1] <= prevWeekHigh or dailyDf['Close'].iloc[-2] <= prevWeekHigh) and currMP > prevWeekHigh:
                    return True
                    
                    
                return False
            else:
                #the symbol has been listed in current week
                return True
        except Exception as e:
            print(e)

        return False

    def isPriceLowerThanPWL(self, symbol):
        '''checks if price is lower than previous month low'''

        try:
            weekDf = yf.download(symbol + ".NS", period="1mo", interval = '1wk', progress= False)
            dailyDf = yf.download(symbol + ".NS", period = '2d', interval = '1d', progress= False)

            currMP = dailyDf['Close'].iloc[-1]

            if(weekDf.size >= 2):
                prevWeekLow = weekDf['Low'].iloc[-2]

                if (dailyDf['Open'].iloc[-1] >= prevWeekLow or dailyDf['Close'].iloc[-2] >= prevWeekLow) and currMP < prevWeekLow:
                    return True
                    
                return False
            else:
                #the symbol has been listed in current month
                return True
        except Exception as e:
            print(e)

        return False

    def check(self):
        while(self.isRunning):
            i = 0

            self.lock.lockForRead()
            while(i < len(SpecialAlertsWorker.stkSymbolsList.index)):
                symbol = SpecialAlertsWorker.stkSymbolsList.index[i]
                self.lock.unlock()

                if self.isPriceCrossingPMH(symbol):
                    if self.checkLastTriggerTime(symbol, 'PMHTriggerTime'):
                        self.sendNotiToDesktop(symbol, ' Price is greater than previous month high')

                        self.notiLock.lockForRead()
                        if(self.teleNoti):
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(symbol +' Price is greater than previous month high'), TeleApiWorker.loop)
                        self.notiLock.unlock()

                    self.setLastTriggerTime(symbol, 'PMHTriggerTime', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

     
                if self.isPriceLowerThanPML(symbol):
                    if self.checkLastTriggerTime(symbol, 'PMLTriggerTime'):
                        self.sendNotiToDesktop(symbol, ' Price is lower than previous month low')

                        self.notiLock.lockForRead()
                        if self.teleNoti :
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(symbol +' Price is lower than previous month low'), TeleApiWorker.loop)
                        self.notiLock.unlock()

                    self.setLastTriggerTime(symbol, 'PMLTriggerTime', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                
                if self.isPriceGreaterThanPWH(symbol):
                    if self.checkLastTriggerTime(symbol, 'PWHTriggerTime'):
                        self.sendNotiToDesktop(symbol, ' Price is greater than previous week high')
                        
                        self.notiLock.lockForRead()
                        if self.teleNoti :
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(symbol +' Price is greater than previous week high'), TeleApiWorker.loop)
                        self.notiLock.unlock()

                    self.setLastTriggerTime(symbol, 'PWHTriggerTime', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                    

                if self.isPriceLowerThanPWL(symbol):
                    if self.checkLastTriggerTime(symbol, 'PWLTriggerTime'):
                        self.sendNotiToDesktop(symbol, ' Price is lower than previous week low')

                        self.notiLock.lockForRead()
                        if self.teleNoti :
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(symbol +' Price is lower than previous week low'), TeleApiWorker.loop)
                        self.notiLock.unlock()

                    self.setLastTriggerTime(symbol, 'PWLTriggerTime', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

                print('scanning of', symbol, 'completed')
                i = i + 1
                self.lock.lockForRead()      
            self.lock.unlock()

            time.sleep(5)  
            print('scanning for special alerts')  

            
    def getAlertsTriggeredStkList(self):
        isNetNotConnectedMsgSend = False

        while(self.isSpecialAlertsPage):
            if(not self.isNetworkConnected()): #if network is not connected
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')
                    isNetNotConnectedMsgSend = True
                continue
            
            isNetNotConnectedMsgSend = False

            today = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0, 0, 0, 0)
            temp = {'stkSymbol': [], 
                                    'PMHBroken': [], 'PMLBroken': [],                             
                                    'PWHBroken': [], 'PWLBroken': []}

            i = 0

            self.lock.lockForRead()
            while(i < len(SpecialAlertsWorker.stkSymbolsList.index)):
                symbol = SpecialAlertsWorker.stkSymbolsList.index[i]

                if (SpecialAlertsWorker.stkSymbolsList['PMHTriggerTime'].loc[symbol] != '' and datetime.strptime(SpecialAlertsWorker.stkSymbolsList['PMHTriggerTime'].loc[symbol], '%Y-%m-%d %H:%M:%S.%f') >= today) or \
                    (SpecialAlertsWorker.stkSymbolsList['PMLTriggerTime'].loc[symbol] != '' and datetime.strptime(SpecialAlertsWorker.stkSymbolsList['PMLTriggerTime'].loc[symbol], '%Y-%m-%d %H:%M:%S.%f') >= today) or \
                    (SpecialAlertsWorker.stkSymbolsList['PWHTriggerTime'].loc[symbol] != '' and datetime.strptime(SpecialAlertsWorker.stkSymbolsList['PWHTriggerTime'].loc[symbol], '%Y-%m-%d %H:%M:%S.%f') >= today) or \
                    (SpecialAlertsWorker.stkSymbolsList['PWLTriggerTime'].loc[symbol] != '' and datetime.strptime(SpecialAlertsWorker.stkSymbolsList['PWLTriggerTime'].loc[symbol], '%Y-%m-%d %H:%M:%S.%f') >= today):
                    
                    temp['stkSymbol'].append(symbol)

                    if(SpecialAlertsWorker.stkSymbolsList['PMHTriggerTime'].loc[symbol] != ''):
                        temp['PMHBroken'].append('YES')
                    else:
                        temp['PMHBroken'].append('NO')

                    if(SpecialAlertsWorker.stkSymbolsList['PMLTriggerTime'].loc[symbol] != ''):
                        temp['PMLBroken'].append('YES')
                    else:
                        temp['PMLBroken'].append('NO')

                    if(SpecialAlertsWorker.stkSymbolsList['PWHTriggerTime'].loc[symbol] != ''):
                        # tempTime = datetime.strptime(SpecialAlertsWorker.stkSymbolsList['PWHTriggerTime'].loc[symbol], '%Y-%m-%d %H:%M:%S.%f').strftime('%I:%M:%S %p')
                        temp['PWHBroken'].append('YES')
                    else:
                        temp['PWHBroken'].append('No')

                    if(SpecialAlertsWorker.stkSymbolsList['PWLTriggerTime'].loc[symbol] != ''):
                        temp['PWLBroken'].append('YES')
                    else:
                        temp['PWLBroken'].append('NO')

                i = i + 1
                self.lock.unlock()
                time.sleep(0.1)
                self.lock.lockForRead()
            self.lock.unlock()

            temp = pd.DataFrame(temp)
            self.sigSpecialAlerts.emit(temp)

            time.sleep(5)
            print('getAlertsTriggeredStkList called')
        
        print('getAlertsTriggeredStkList finished')
        self.finished.emit()

class MyOrdersWorker(QObject):
    myOrders = { "status": "success", "data": []}   #static variable to share holdings for all objects
    isRunning = True
    isNetConnected = True

    sigChngMyOrdersData = Signal(pd.DataFrame)   #signals to communicate with other threads
    sigMyOrdersDetails = Signal(pd.DataFrame) #signal to emit holding details to be shown on home page
    sigShowMsg = Signal(str)
    finished = Signal() 

    def __init__(self, key='', sKey='', brCode='tc'):
        super().__init__()
        self.lock = QReadWriteLock()
        self.apiKey = key
        self.apiSecretKey = sKey
        self.brCode = brCode

        self.pendingOrdersCnt = 0
        self.closedOrdersCnt = 0
        self.rejectedOrdersCnt = 0
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)

        #to show myOrders in myOrders page
        self.isMyOrdersPage = False

    def changeDetails(self, key='', sKey='', brCode = 'tc'):
        self.apiKey = key
        self.apiSecretKey = sKey
        self.brCode = brCode
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)            

    def fetchAllOrders2(self):
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
        
    def fetchMyOrders(self):
        while(MyOrdersWorker.isRunning):
            try :
                self.lock.lockForWrite()
                MyOrdersWorker.myOrders = json.loads(json.dumps(self.algomojo.OrderBook(broker = self.brCode)))
                # MyOrdersWorker.myOrders = self.fetchAllOrders2()
                self.lock.unlock()
                
                self.lock.lockForRead()
                if(MyOrdersWorker.myOrders['status'] == 'success'):
                    orders = pd.DataFrame(MyOrdersWorker.myOrders['data'])
                    # orders.drop(['ws_msg'], axis = 1, inplace= True)

                    successfulOrdersFilter = orders['status'] == 'completed'
                    rejectedOrdersFilter = orders['status'] == 'rejected'
                    cancelledOrdersFilter = orders['status'] == 'cancelled'
                    pendingOrdersFilter = orders['status'] == 'pending'
                    openOrdersFilter = orders['status'] == 'open'

                    '''for Pending orders'''
                    pendingOrders = orders.where(pendingOrdersFilter) #filter pending orders
                    pendingOrders.dropna(axis= 0, inplace= True) #after filtering the resultant df will place Na values in place of other records threfore remove records containing na values
                    self.pendingOrdersCnt = len(pendingOrders)

                    '''for Closed orders'''
                    closedOrders = orders.where(successfulOrdersFilter) #filter pending orders
                    closedOrders.dropna(axis= 0, inplace= True) #after filtering the resultant df will place Na values in place of other records threfore remove records containing na values
                    self.closedOrdersCnt = len(closedOrders)

                    '''for Rejected orders'''
                    rejectedOrders = orders.where(rejectedOrdersFilter) #filter pending orders
                    rejectedOrders.dropna(axis= 0, inplace= True) #after filtering the resultant df will place Na values in place of other records threfore remove records containing na values
                    self.rejectedOrdersCnt = len(rejectedOrders)

                    self.sigMyOrdersDetails.emit( pd.DataFrame({'pendingOrdersCnt': [self.pendingOrdersCnt], 'closedOrdersCnt': [self.closedOrdersCnt], 'rejectedOrdersCnt': [self.rejectedOrdersCnt]})) #emit data to show on home page
                
                else:
                    print(MyOrdersWorker.myOrders['error_msg'])
                self.lock.unlock()
                MyOrdersWorker.isNetConnected = True
            except requests.exceptions.ConnectionError:
                self.lock.unlock()
                MyOrdersWorker.isNetConnected = False
            except Exception as e:
                print(e)
            
            print('MyOrdersfetchingThread called')
            time.sleep(5)
    
    def getMyOrdersTableModel(self):
        isApiInvalidMsgShown = False 
        isNetNotConnectedMsgSend = False
        
        while(self.isMyOrdersPage):
            if(not MyOrdersWorker.isNetConnected): #if network is not connected
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')
                    isNetNotConnectedMsgSend = True
                continue

            self.lock.lockForRead()
            if(MyOrdersWorker.myOrders['status'] == 'success'):
                self.sigChngMyOrdersData.emit(pd.DataFrame(MyOrdersWorker.myOrders['data']))

                isApiInvalidMsgShown = False
            else:
                if(not isApiInvalidMsgShown):
                    #show message
                    self.sigShowMsg.emit(MyOrdersWorker.myOrders['error_msg'])
                    isApiInvalidMsgShown = True
            
            self.lock.unlock()
            isNetNotConnectedMsgSend = False

            time.sleep(5)
            print("getMyOrdersTbleModel function ")

        self.finished.emit()
        print('getMyOrdersTbleModel finished')
