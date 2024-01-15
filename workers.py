from urllib import request
from PySide6.QtCore import QObject, Signal

import mysql.connector
from mysql.connector import errorcode
from APIMethods import getQuote2, getQuote, getHoldings2, getQuoteFromYfinance
import json
import math
import time
import zroya
import talib
import yfinance as yf
import pandas as pd
from algomojo.pyapi import *
import copy
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
            await client.send_message('+918208823690', msg)

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
    isRunning = False
    alertList = []

    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    noti.setAudio(audio=zroya.Audio.Alarm)
    
    tf = {'Daily' : '1d', 'Monthly' : '1mo', 'Weekly' : '1wk'}
    def getAlertList():
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select * from alerts"""
            cursor.execute(query)
            alerts = []
            for (sym, name, type, condition, tf, val, len1, len2, msg, isPaused) in cursor:
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
    
    def myAction(self, nId, actionId):
        if(actionId == 0):
            print("stock sold successfully")
        elif(actionId == 1):
            print("Thank you for response")

    def sendNotiToDesktop(self, title, message):
        self.noti.setFirstLine(title) 
        self.noti.setSecondLine(message)
        self.noti.addAction("sell")
        self.noti.addAction("No")
        zroya.show(self.noti, on_action= self.myAction) #notificatoin sent to desktop
        # zroya.show(self.noti) #notificatoin sent to desktop

    def processAlerts(self):
        isSentNetworkWarning = False
        while(self.isRunning):
            for alert in AlertWorker.alertList:
                if(alert['isPaused']):
                    continue

                if(not isNetworkConnected()):
                    if(not isSentNetworkWarning):
                        isSentNetworkWarning = True
                        print('check network')
                else:
                    isSentNetworkWarning = False


                try:
                    # currPrice = json.loads(getQuote2('shubh',alert['stkSymbol'], 'tc', 'NSE'))['data']['close']
                    currPrice = getQuoteFromYfinance('shubh',alert['stkSymbol'], 'tc', 'NSE')['Close'].iloc[-1]
                except Exception as e:
                    print(e)
                    continue

                match alert['alertCond']:
                    case 'Greater Than':
                        if alert['alertType'] == 'Price':
                            if currPrice > alert['alertVal']:
                                print(alert['stkName'], 'price is greater than ', alert['alertVal'])

                                title = alert['stkName']
                                msg = str(str(alert['stkName']) + ' price is greater than ' + str(alert['alertVal']))
                                self.sendNotiToDesktop(title, msg)
                                asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)

                                self.pauseAlert(alert) #pause alert when 1 notification is sent

                        elif alert['alertType'] == 'MA' or alert['alertType'] == 'Price + EMA' or alert['alertType'] == 'Price + HMA':
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                            Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                            if currPrice > Avg[-1]:
                                print(alert['stkName'], 'price is greater than EMA', alert['len1'])

                                title = alert['stkName']
                                msg = str(str(alert['stkName']) + ' price is greater than EMA' + str(alert['len1']))
                                self.sendNotiToDesktop(title, msg)
                                asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)

                                self.pauseAlert(alert) #pause alert when 1 notification is sent
                                
                    case 'Less Than':
                        if alert['alertType'] == 'Price':
                            if currPrice < alert['alertVal']:
                                print(alert['stkName'], 'price is less than ', alert['alertVal'])

                                title = alert['stkName']
                                msg = str(str(alert['stkName']) + ' price is less than ' + str(alert['alertVal']))
                                self.sendNotiToDesktop(title, msg)
                                asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)
                                
                                self.pauseAlert(alert) #pause alert when 1 notification is sent

                        elif alert['alertType'] == 'MA' or alert['alertType'] == 'Price + EMA' or alert['alertType'] == 'Price + HMA':
                            stk = yf.Ticker(alert['stkSymbol']+".NS")
                            df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                            Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                            if currPrice < Avg[-1]:
                                print(alert['stkName'], 'price is greater than EMA', alert['len1'])

                                title = alert['stkName']
                                msg = str(str(alert['stkName']) + ' price is greater than EMA' + str(alert['len1']))
                                self.sendNotiToDesktop(title, msg)
                                asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)

                                self.pauseAlert(alert) #pause alert when 1 notification is sent

                    case 'Crossing Up':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], alert['timeFrame'], alert['len1'])

                        if((df['Open'][-1] < Avg[-1] or df['Close'][-2] < Avg[-2]) and df['Close'] > Avg[-1]):
                            print(alert['stkName'], 'crosses up the price ', alert['alertVal'])

                            title = alert['stkName']
                            msg = str(str(alert['stkName']) + ' crosses up the price ' + str(alert['alertVal']))
                            self.sendNotiToDesktop(title, msg)
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)


                            self.pauseAlert(alert) #pause alert when 1 notification is sent

                    case 'Crossing Down':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['len1']])

                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len1'])

                        if((df['Open'][-1] > Avg[-1] or df['Close'][-2] > Avg[-2]) and df['Close'] < Avg[-1]):
                            print(alert['stkName'], 'crosses down the price ', alert['alertVal'])

                            title = alert['stkName']
                            msg = str(str(alert['stkName']) + ' crosses down the price ' + str(alert['alertVal']))
                            self.sendNotiToDesktop(title, msg)
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)


                            self.pauseAlert(alert) #pause alert when 1 notification is sent

                    case 'Price > PrevMonthHigh':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'], alert['len1'])

                        currMP = df['Close'].iloc[-1]
                        prevHigh = max(df['Close'][-2], df['Close'][-3])
                        if Avg[-1] > Avg[-2] and Avg[-2] > Avg[-3]: #uptrend
                            if currMP > prevHigh :
                                print(alert['stkName'], 'Breaks the previous month high of')

                                title = alert['stkName']
                                msg = str(str(alert['stkName']) + ' Breaks the previous month high')
                                self.sendNotiToDesktop(title, msg)
                                asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)

                                self.pauseAlert(alert) #pause alert when 1 notification is sent

                    case 'Price < PrevMonthLow':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])
                        
                        Avg = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len1'])

                        currMP = df['Close'].iloc[-1]
                        prevLow = min(df['Close'][-2], df['Close'][-3])
                        if Avg[-1] < Avg[-2] and Avg[-2] < Avg[-3]: #downtrend
                            if currMP < prevLow :
                                print(alert['stkName'], 'Breaks the previous month low')

                                title = alert['stkName']
                                msg = str(str(alert['stkName']) + ' Breaks the previous month low')
                                self.sendNotiToDesktop(title, msg)
                                asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)

                                self.pauseAlert(alert) #pause alert when 1 notification is sent

                    case 'In Between':
                        stk = yf.Ticker(alert['stkSymbol']+".NS")
                        df = stk.history(period="max", interval = self.tf[alert['timeFrame']])

                        #EMAs        
                        Avg1 = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len1'])
                        Avg2 = self.calAverage(df['Close'].to_numpy(), alert['alertType'], 
                                alert['timeFrame'],   alert['len2'])
                        currMP = df['Close'].iloc[-1] 
                        if (currMP < Avg1[-1] and currMP > Avg2[-1]) or (currMP > Avg1[-1] and currMP < Avg2[-1]):
                            print('Price of ' , alert['stkName'], 'is in between', 'EMA'+str(alert['len1']), 'and', 'EMA'+str(alert['len2']))

                            title = alert['stkName']
                            msg = str('Price of ' + str(alert['stkName']) + ' is in between ' + 'EMA'+ str(alert['len1']) + ' and ' + 'EMA'+str(alert['len2']))
                            self.sendNotiToDesktop(title, msg)
                            asyncio.run_coroutine_threadsafe(TeleApiWorker.sendMessage(msg), TeleApiWorker.loop)

                            self.pauseAlert(alert) #pause alert when 1 notification is sent

            time.sleep(5)
            # self.getAlertList()
            print("processAlerts Called")
      

class HoldingsWorker(QObject):
    zroya.init("StockAutomation", "a", "b", "c", "d")
    noti = zroya.Template(zroya.TemplateType.Text2)
    # noti.setAudio(audio=zroya.Audio.Alarm)

    holdings = { "status": "success", "data": []}   #static variable to share holdings for all objects
    isRunning = True
    isNetConnected = False

    sigChngHoldData = Signal(pd.DataFrame)   #signals to communicate with other threads
    sigNoHoldData = Signal()
    sigShowMsg = Signal(str)
    finished = Signal()

    def __init__(self, key='', sKey='', brCode='tc'):
        super().__init__()
        self.apiKey = key
        self.apiSecretKey = sKey
        self.brCode = brCode
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)

        #to show holdings in holdings page
        self.isHoldingsPage = False

    def changeDetails(self, key, sKey, brCode = 'tc'):
        self.apiKey = key
        self.apiSecretKey = sKey
        self.brCode = brCode
        self.algomojo = api(api_key = self.apiKey, api_secret= self.apiSecretKey)
        
    
    def fetchHoldings(self, brCode = 'tc'):
        while(HoldingsWorker.isRunning):
            try :
                HoldingsWorker.holdings = json.loads(json.dumps(self.algomojo.Holdings(broker=brCode)))
                
                # print(HoldingsWorker.holdings['status'])
                # print(HoldingsWorker.holdings['error_msg'])
                # print(HoldingsWorker.holdings['error_type'])

                # HoldingsWorker.holdings = self.algomojo.Holdings(broker=brCode) #use above if this not work
                # HoldingsWorker.holdings = getHoldings2() #testing purpose only

                HoldingsWorker.isNetConnected = True
            except requests.exceptions.ConnectionError:
                HoldingsWorker.isNetConnected = False
            except Exception as e:
                print(e)
            

            print('HoldingsfetchingThread called')
            time.sleep(5)

    def myAction(nId, actionId):
        if(actionId == 0):
            print("stock sold successfully")
        elif(actionId == 1):
            print("Thank you for response")

    def processHoldings(self):
        while(HoldingsWorker.isRunning):
            myData = HoldingsWorker.holdings

            if(myData['status'] == 'success'):
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
            print("process Holdings called")                            

    def getHoldingsTableModel(self):
        self.isApiInvalidMsgShown = False 
        isNetNotConnectedMsgSend = False
        
        while(self.isHoldingsPage):
            if(not HoldingsWorker.isNetConnected): #if network is not connected
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')
                    isNetNotConnectedMsgSend = True
                continue

            self.myData = HoldingsWorker.holdings

            if(self.myData['status'] == 'success'):
                if(len(self.myData['data']) != 0):
                    self.dfHoldings = pd.DataFrame(self.myData['data'], columns=['symbol', 'holdqty','average_price','invest_val','hld_val','PL'])
                    self.sigChngHoldData.emit(self.dfHoldings)
                else:
                    self.sigNoHoldData.emit()
                
                self.isApiInvalidMsgShown = False
            else:
                if(not self.isApiInvalidMsgShown):
                    #show message
                    self.sigShowMsg.emit(self.myData['error_msg'])
                    self.sigNoHoldData.emit()
                    self.isApiInvalidMsgShown = True
            
            isNetNotConnectedMsgSend = False

            time.sleep(5)
            print("getHoldingTbleModel function ")

        self.finished.emit()
        print('getHoldingTbleModel finished')

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

    def getWLSymbols(self, watchlist):
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='watchlists_db')
            cursor = con.cursor()
            query = f"""select * from {watchlist}"""
            cursor.execute(query)

            for stkSym, stkName in cursor:
                self.stkList[stkSym] = stkName

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            con.close()

    def fetchWLData(self):    
        data = {'Symbol' : [], 'Name' : [], 'Open' : [], 'High' : [], 'Low' : [], 'Close' : []}
        
        stkList = copy.deepcopy(self.stkList)
        
        for key in stkList.keys():
            if(not isNetworkConnected()): #if network is not connected stop the operation
                break

            if(self.isRunning == False or self.isWLChanged): #watchlist closed or watchlist changed
                break

            # importing data from yfinance
            try:
                hist = yf.download(key + '.NS', period='1d', interval='1d')

                # #item method is used to retrieve data only else it return data with index
                open =  round(hist['Open'].item(), 2)
                high =  round(hist['High'].item(), 2)
                low =  round(hist['Low'].item(), 2)
                close =  round(hist['Close'].item(), 2)

                data['Symbol'].append(key)
                data['Name'].append(stkList[key])
                data['Open'].append(open)
                data['High'].append(high)
                data['Low'].append(low)
                data['Close'].append(close)
            except Exception as e:
                print('Exception in watchlist thread', e)

        return pd.DataFrame(data)
        
    def updateWL(self):
        isNetNotConnectedMsgSend = False
        while(self.isRunning):
        # for i in range(3):
            if(isNetworkConnected()):
                data = self.fetchWLData()

            if(isNetworkConnected()):
                self.sigShowWLData.emit(data)
                isNetNotConnectedMsgSend = False
            else:
                if(not isNetNotConnectedMsgSend):
                    self.sigShowMsg.emit('Please check your internet connection')
                    isNetNotConnectedMsgSend = True

            if(self.isRunning == False): #watchlist closed
                continue
            
            if(self.isWLChanged): #if watchlist changed
                self.stkList.clear()
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
        self.sigShowWLData.emit(pd.DataFrame({'Symbol' : [], 'Name' : [], 'Open' : [], 'High' : [], 'Low' : [], 'Close' : []}))


class StockWorker(QObject):
    sigShowStkDetails = Signal(pd.DataFrame)
    sigShowCheckNetworkMsg = Signal(str)
    finished = Signal()

    def __init__(self, name):
        super().__init__()
        self.stkSymbol = name
        self.isRunning = True

    def fetchStockDetails(self):
        isNetNotConnectedMsgSend = False
        while(self.isRunning):
            try:
                stkDf = yf.download(self.stkSymbol + '.NS', period='1d', interval='1d')
                stk = yf.Ticker(self.stkSymbol + '.NS')
                stkInfo = stk.info
                self.sigShowStkDetails.emit(pd.DataFrame({'Open': stkDf['Open'], 
                                                        'High': stkDf['High'], 
                                                        'Low': stkDf['Low'], 
                                                        'Close': stkDf['Close'], 
                                                        'Volume': stkDf['Volume'], 
                                                        'fiftyTwoWeekHigh': stkInfo['fiftyTwoWeekHigh'], 
                                                        'fiftyTwoWeekLow': stkInfo['fiftyTwoWeekLow'] 
                                                        }))
                isNetNotConnectedMsgSend = False    
            except requests.exceptions.ConnectionError:
                if(not isNetNotConnectedMsgSend):
                    self.sigShowCheckNetworkMsg.emit('Please check your internet connection')   
                    isNetNotConnectedMsgSend = True                                 
            except Exception as e:
                print('Exception in stkDetailsWorker', e)

            print('fetchStockDetails called')
            time.sleep(5)

        self.finished.emit()
        print('fetchStockDetails thread ended')
