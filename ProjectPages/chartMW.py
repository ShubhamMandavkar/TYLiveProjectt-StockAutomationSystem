from PySide6.QtWidgets import QMainWindow, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCavas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import math
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
import pandas as pd
import talib
import mysql.connector
from mysql.connector import errorcode
import matplotlib.dates as mpdates
from matplotlib.widgets import Cursor
import matplotlib.animation as animation
from mpl_interactions import ioff, panhandler, zoom_factory
from matplotlib.backend_bases import MouseEvent
import datetime
from dateutil.relativedelta import relativedelta  

from UIFiles.ui_chart import Ui_Chart
from ProjectPages.indicatorDetailsDlg import IndicatorDetailsDlg
from ProjectPages.deleteIndicatorDlg import DeleteIndicatorDlg

class StockChart(FigCavas):
    panning = False
    start_x = None
    start_y = None
    dictTimeIntervals = {'1 minute' : '1m', '2 minute' : '2m', '5 minute' : '5m', '15 minute' : '15m', 
                            '30 minute' : '30m', '60 minute' : '60m', '90 minute' : '90m', '1 day' : '1d',
                            '5 day' : '5d', '1 week' : '1wk', '1 month' : '1mo', '3 month' : '3mo'}

    dictPeriods = {'1 minute' : '7d', '2 minute' : '60d', '5 minute' : '60d', '15 minute' : '60d', 
                            '30 minute' : '60d', '60 minute' : '2y', '90 minute' : '60d', '1 day' : 'max',
                            '5 day' : 'max', '1 week' : 'max', '1 month' : 'max', '3 month' : 'max'}

    def __init__(self, symbol, name):  
        self.stkSymbol = symbol
        self.stkName = name

        # creating Subplots
        self.fig = mpf.figure(figsize=(12,9))
        super().__init__(self.fig)

        self.period = 'max'
        self.timeFrame = '1d'

        self.ax = self.fig.subplots()
        self.plotChart(self.timeFrame, self.period)

        # setting title
        # plt.title(self.stkName)
        
        self.fig.tight_layout()

        disconnect_zoom = zoom_factory(self.ax)
        # Enable scrolling and panning with the help of MPL
        # Interactions library function like panhandler.
        # pan_handler = panhandler(self.fig) #if this is enabled then it stop the zoom in x axis and y axis
       
        # self.growingCandleAnimation()

    def plotChart(self, timeFrame, myPeriod):
        '''importing data from yfinance'''
        stk = yf.Ticker(self.stkSymbol+".NS")
        hist = stk.history(period = myPeriod, interval = timeFrame)

        self.df = pd.DataFrame({'Date': hist.index, 'Open': hist['Open'],'High': hist['High'], 'Low':hist['Low'], 'Close':hist['Close']})
        # convert into datetime object
        self.dates = pd.to_datetime(hist.index)
        self.df['Date'] = pd.to_datetime(hist.index)

        # apply map function
        self.df['Date'] = self.df['Date'].map(mpdates.date2num)
        '''ended importing code'''
        print('data imported')

        # plotting the data
        self.ax.clear()          #clear the axes
        #scale the graph to the last 100 candles
        self.ax.set_xlim(len(self.df.index)-100, len(self.df.index))

        mpf.plot(self.df, type='candle', ax=self.ax) #plots candlestick chart
        plt.draw()
        # plt.pause(0.1) #if called then matplotlib displays it's own figure window

        # Setting labels
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Price')
        

        # Add a vertical line to show the current candle
        # because the axis has been cleared the line must be redrawn
        self.vline = self.ax.axvline(x=0, color='r', linestyle='--', label='Vertical Line', linewidth=1) 
        self.vline.set_visible(False)
        
        #Add dateTick on xaxis
        self.dateTick = self.ax.text(0, -0.05, '', color = 'white',  transform = self.ax.get_xaxis_transform(), ha='center', va='top', bbox=dict(facecolor='grey', alpha=1))
        
        print('chart shown')

    #get data for daily, weekly, or monthly dataFrame   
    def getData(self, i):
        '''importing data from yfinance'''
        stk = yf.Ticker(self.stkSymbol+".NS")
        hist = stk.history(period = '1d', interval = '1d')

        df = pd.DataFrame({'Date': hist.index, 'Open': hist['Open'],'High': hist['High']+i, 'Low':hist['Low'], 'Close':hist['Close']+i})
        # convert into datetime object
        df['Date'] = pd.to_datetime(hist.index)

        # apply map function
        df['Date'] = df['Date'].map(mpdates.date2num)
        print(df['Date'])
        '''ended importing code'''

        print('data imported')
        
        return df

    def growingCandleAnimation(self):
        resample_map ={'Open' :'first', 'High' :'max', 'Low'  :'min', 'Close':'last' }
        resample_period = '15T'   

        self.i = 5
        def animate(ival):
            df = self.getData(self.i)

            # rs = df.resample(resample_period).agg(resample_map).dropna()
            self.df = self.df.iloc[:-1]
            self.df = pd.concat([self.df, df])
            self.ax.clear()
            mpf.plot(self.df, ax = self.ax, type='candle')
            self.i = self.i+ 5
            print('animation called')

        self.ani = animation.FuncAnimation(self.fig, animate, interval=2500, cache_frame_data=False)


    def setTimeFrame(self, timeFrame):
        self.timeFrame= self.dictTimeIntervals[timeFrame] 
        self.period = self.dictPeriods[timeFrame]
        
        self.plotChart(self.timeFrame, self.period) #plot the changed timeFrame chart

    
    def showSignals(self):
        pltLs = []

        #EMAs        
        EMA9 = talib.EMA(self.df['Close'].to_numpy(), timeperiod=9)
        EMA14 = talib.EMA(self.df['Close'].to_numpy(), timeperiod=14)

        signal1 =[low if ((low < e1 and low > e2) or (low > e1 and low < e2)) else np.nan for low, e1, e2 in zip(self.df['Low'], EMA9,EMA14)]

        
        PMHSignal = []  #previous month high signal
        PMLSignal = []  #previous month Low signal

        self.monthDf = pd.DataFrame({'Date': [], 'Open': [],'High': [], 'Low': [], 'Close': []})
        stk = yf.Ticker(self.stkSymbol+".NS")
        hist = stk.history(period = 'max', interval = '1mo')

        self.monthDf = pd.DataFrame({'Date': pd.to_datetime(hist.index), 'Open': hist['Open'],'High': hist['High'], 'Low':hist['Low'], 'Close':hist['Close']})

        
        EMA50 = talib.EMA(self.monthDf['Close'].to_numpy(), timeperiod=50)  
            
        # prevHigh = self.monthDf['High'].iloc[0]
        prevLow = self.df['Low'].iloc[0]

        i = 0
        j= 0

        m1, year1 = str(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m %Y')).split(' ')
        m1 = int(m1)
        year1 = int(year1)
        m2, year2 = str(datetime.datetime.strftime(self.dates[j], '%m %Y')).split(' ')
        m2 = int(m2)
        year2 = int(year2)

        if(year1 == year2):
            while(m2 > m1 and m1 != m2-1):
                i = i+1
                m1 = int(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m'))
        else:
            if(m2 == 1):
                while(year1 != year2-1):
                    i = i+1
                    m1, year1 = str(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m %Y')).split(' ')
                    m1 = int(m1)
                    year1 = int(year1)
                while(m1 != 12):
                    i = i+1
                    m1 = int(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m'))
            else:
                while(year1 != year2):
                    i = i+1
                    m1, year1 = str(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m %Y')).split(' ')
                    m1 = int(m1)
                    year1 = int(year1)
                while(m2 > m1 and m1 != m2-1):
                    i = i+1
                    m1 = int(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m')) 

        while(j < len(self.df)):
            m1 = int(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m'))
            m2 = int(datetime.datetime.strftime(self.dates[j], '%m'))

            while(m1 == m2):
                j = j+1
                if(j == len(self.df)):
                    break

                m2 = int(datetime.datetime.strftime(self.dates[j], '%m'))
                PMHSignal.append(np.nan)
                PMLSignal.append(np.nan)

            
            while(abs(m1 - m2) > 1 and (m1+1)%12 != m2):
                i = i+1
                m1 = int(datetime.datetime.strftime(self.monthDf['Date'].iloc[i], '%m'))
                # print('myCalled--------------------', m1, year1, m2, year2, j)

            # print(EMA50[i], EMA50[i-1], EMA50[i-2], i)

            if EMA50[i] > EMA50[i-1] and EMA50[i-1] > EMA50[i-2]: 
                print(self.df['High'].iloc[j], self.monthDf['High'].iloc[i])
                if self.df['High'].iloc[j] > self.monthDf['High'].iloc[i]:
                    PMHSignal.append(self.df['High'].iloc[j] + 5) # +5 added to show signal little bit above candle
                else:
                    PMHSignal.append(np.nan)
            else:
                PMHSignal.append(np.nan)
            
            if EMA50[i] < EMA50[i-1] and EMA50[i-1] < EMA50[i-2]: 
                if self.df['Low'].iloc[i] < prevLow :
                    PMLSignal.append(self.df['Low'].iloc[i] + 5) # +5 added to show signal little bit above candle
                    prevLow = self.df['Low'].iloc[i]
                else:
                    PMLSignal.append(np.nan)
            else:
                prevLow = self.df['Low'].iloc[i]
                PMLSignal.append(np.nan)

            j = j+1


        #end PMHSignal
        # line1, = plt.plot(self.df['Date'], self.df['Close'], color='black')
        pltLs.append(mpf.make_addplot(signal1, ax = self.ax, type = 'scatter', marker = '^', 
                        markersize = 50, color = 'r')) 
        pltLs.append(mpf.make_addplot(PMHSignal, ax = self.ax, type = 'scatter', marker = 'D', 
                        markersize = 50, color = 'g')) 
        pltLs.append(mpf.make_addplot(PMLSignal, ax = self.ax, type = 'scatter', marker = 'D', 
                        markersize = 50, color = 'r')) 

        mpf.plot(self.df, ax = self.ax, type='candle', addplot = pltLs)
        plt.draw()

    def addIndicator(self, indicator, length):
        pltLs = []
        match indicator:
            case 'RSI':                                                 #work in progress(incomplete)
                rsi  = talib.RSI(self.df['Close'].to_numpy()) 
                rsiPlt = mpf.make_addplot(rsi, ax = self.fig.add_subplot(self.ax), panel = 1)
                mpf.plot(self.df, ax= self.ax, type='candle', addplot = rsiPlt, panel_ratios = (.8, .2))
                plt.draw()

                # rsiAx = self.fig.add_subplot(2,1, 1, sharex = self.ax)
                # rsiPlt = mpf.make_addplot(rsi, ax = rsiAx, panel = 2)
                # mpf.plot(self.df, ax = self.ax, type = 'candle', addplot = rsiPlt, panel_ratios = (.8, .2), main_panel = 0, num_panels = 3)
                # plt.draw()

            case 'Exponential Moving Average':
                EMA = talib.EMA(self.df['Close'].to_numpy(), timeperiod= length)

                pltLs.append(mpf.make_addplot(EMA, ax = self.ax))
                print('Exponential moving average plotted')

            case 'Hull Moving Average':
                HMA = talib.WMA(2*talib.WMA(self.df['Close'], timeperiod = length/2)-talib.WMA(self.df['Close'], timeperiod = length), timeperiod = math.floor(math.sqrt(length)))
                pltLs.append(mpf.make_addplot(HMA, ax = self.ax))
 
                HMASignal = [self.df['Close'].iloc[i] if (self.df['Close'].iloc[i] > HMA[i] and self.df['Open'].iloc[i] < HMA[i]) or (self.df['Close'].iloc[i-1] < HMA[i-1] and self.df['Open'].iloc[i] > HMA[i]) else np.nan for  i in range(1,len(self.df['Close']))]

                HMASignal.insert(0, np.nan)
                # pltLs.append(mpf.make_addplot(HMASignal, ax = self.ax, type = 'scatter', marker = '^', 
                #         markersize = 50, color = 'b')) temporarily commented for the seminar purpose
                print('Hull Moving Average')

        mpf.plot(self.df, ax = self.ax, type='candle', addplot = pltLs)
        plt.draw()
        
    def on_mouse_press(self, event):
        if event.button == 1:  # Left mouse button
            self.panning = True
            self.start_x = event.xdata
            self.start_y = event.ydata    
            print('panning start')  

    def on_mouse_release(self, event):
        self.panning = False
        print('panning end')  

    def on_mouse_move(self, event):
        if self.panning:
            dx = event.xdata - self.start_x
            dy = event.ydata - self.start_y
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
            self.ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
            plt.draw()

class Chart(QMainWindow):
    def __init__(self, stkSym, stkName, parent=None):
        super().__init__(parent)
        self.ui = Ui_Chart()
        self.ui.setupUi(self)

        self.stkSymbol = stkSym
        self.stkName = stkName

        self.ui.lblStkName.setText(self.stkName)
        self.ui.frmCandleDetails.setMinimumHeight(40)
        self.showChart()
        self.addConnectors()
    
    #This method is used to connect slots to the signals generated by ui components
    def addConnectors(self):
        self.ui.cmbTimeFrame.currentTextChanged.connect(self.changeTimeFrame)
        self.ui.cmbIndicators.textActivated.connect(self.showIndicatorsDetailsDlg) 
        self.ui.cmbIndicatorsAdded.textActivated.connect(self.deleteIndicator)

        # Connect the function to the motion_notify_event
        self.stkChart.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move2)   

        # below code is implemented for panning the chart with only mouse
        # self.chart.fig.canvas.mpl_connect('button_press_event', self.chart.on_mouse_press)
        # self.chart.fig.canvas.mpl_connect('button_release_event', self.chart.on_mouse_release)
        # self.chart.fig.canvas.mpl_connect('motion_notify_event', self.chart.on_mouse_move)

    def showChart(self):
        self.stkChart = StockChart(self.stkSymbol, self.stkName)
        self.toolbar = NavigationToolbar(self.stkChart, self.ui.frmChart)
        self.chartVerticalLayout = QVBoxLayout(self.ui.frmChart)
        self.chartVerticalLayout.setObjectName(u"verticalLayout")
        self.chartVerticalLayout.addWidget(self.stkChart)
        self.chartVerticalLayout.addWidget(self.toolbar)

        self.renderChartState()
        # self.stkChart.showSignals()   

    #This methods addds the indicators to the chart which were added by to user to show the saved state
    def renderChartState(self):     
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            query = f"""select * from chart_state"""
            cursor.execute(query)
            self.ui.cmbIndicatorsAdded.clear()
            for indicator, len, color in cursor:
                self.stkChart.addIndicator(indicator, len)
                self.ui.cmbIndicatorsAdded.addItem(indicator + '.' + str(len))

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
    
    def changeTimeFrame(self):
        self.stkChart.setTimeFrame(self.ui.cmbTimeFrame.currentText())
        self.renderChartState()
        self.stkChart.showSignals()
    
    def showIndicatorsDetailsDlg(self):
        if self.ui.cmbIndicators.currentText() == 'None':
            return

        self.dlgIndicatorDetails = IndicatorDetailsDlg()
        self.dlgIndicatorDetails.show()

        def saveDetails():
            length = self.dlgIndicatorDetails.ui.sbLen.value()
            indicator = self.ui.cmbIndicators.currentText()

            self.stkChart.addIndicator(indicator, length)

            #save chart state in Database
            try:
                con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
                cursor = con.cursor()

                query = f"""insert into chart_state values('{indicator}', {length}, 'null') """
                cursor.execute(query)
                con.commit()

                #show the indicator in the added indicators combobox
                self.ui.cmbIndicatorsAdded.addItem(indicator + '.' + str(length))
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


        self.dlgIndicatorDetails.ui.bbOkCancel.accepted.connect(saveDetails)

    def deleteIndicator(self):
        indicator , length = self.ui.cmbIndicatorsAdded.currentText().split('.')
        ind = self.ui.cmbIndicatorsAdded.currentIndex()
        self.dlgDeleteIndicator = DeleteIndicatorDlg(indicator, int(length))
        self.dlgDeleteIndicator.show()

        #delete from Database
        def deleteIndicatorFrmDB():
            try:
                con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
                cursor = con.cursor()

                query = f"""delete from chart_state where indicator = '{indicator}' and length = {length}"""
                cursor.execute(query)
                con.commit()

                self.dlgDeleteIndicator.close()

                self.stkChart.plotChart(self.stkChart.timeFrame, self.stkChart.period)
                self.renderChartState() 
                # self.stkChart.showSignals()

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

        def closeDlg():
            self.dlgDeleteIndicator.close()

        self.dlgDeleteIndicator.ui.btnDelete.clicked.connect(deleteIndicatorFrmDB)
        self.dlgDeleteIndicator.ui.btnCancel.clicked.connect(closeDlg)

    #this method shows date of current candle and OHLC details on mouse move in chart
    def on_mouse_move2(self, event):
        # Check if the cursor is within the axes limits
        if event.inaxes:
            #make line visible
            self.stkChart.vline.set_visible(True)

            # Update the vertical line position (optional)
            self.stkChart.vline.set_xdata(math.ceil(event.xdata)) #display coordinated


            #set dateTick visibility to false if cursor is in the valid range then it will be make visible
            self.stkChart.dateTick.set_visible(False) #make dateTick invisible
            
            if math.ceil(event.xdata) >= 0 and math.ceil(event.xdata) < len(self.stkChart.df):
                xdata = min(math.ceil(event.xdata), len(self.stkChart.df)-1)#diplay coordinate of xaxis

                #code to show current date on xaxis 
                self.stkChart.dateTick.set_visible(True) #make dateTick visible

                currdate = self.stkChart.df.index[xdata] # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
                ts = pd.Timestamp(currdate) #converted to pandas Timestamp
                tf = self.stkChart.timeFrame
                if('mo' in tf or 'wk' in tf or 'd' in tf):
                    self.stkChart.dateTick.set_text(ts.strftime('%d %b %Y')) #formated date
                else:
                    self.stkChart.dateTick.set_text(ts.strftime('%d %b %Y %H:%M')) #formated date
                self.stkChart.dateTick.set_x(event.xdata)  #display coordinates
                
                self.ui.lblOpenVal.setText(str(format(self.stkChart.df['Open'].iloc[xdata],'.2f')))
                self.ui.lblHighVal.setText(str(format(self.stkChart.df['High'].iloc[xdata],'.2f')))
                self.ui.lblLowVal.setText(str(format(self.stkChart.df['Low'].iloc[xdata],'.2f')))
                self.ui.lblCloseVal.setText(str(format(self.stkChart.df['Close'].iloc[xdata],'.2f')))
            elif math.ceil(event.xdata) >= len(self.stkChart.df):
                self.ui.lblOpenVal.setText(str(format(self.stkChart.df['Open'].iloc[-1],'.2f')))
                self.ui.lblHighVal.setText(str(format(self.stkChart.df['High'].iloc[-1],'.2f')))
                self.ui.lblLowVal.setText(str(format(self.stkChart.df['Low'].iloc[-1],'.2f')))
                self.ui.lblCloseVal.setText(str(format(self.stkChart.df['Close'].iloc[-1],'.2f')))
            else: #math.ceil(event.xdata) < 0
                self.ui.lblOpenVal.setText('$')
                self.ui.lblHighVal.setText('$')
                self.ui.lblLowVal.setText('$') 
                self.ui.lblCloseVal.setText('$')
            
            # Redraw the figure
            self.stkChart.fig.canvas.draw()
        else:
            self.stkChart.vline.set_visible(False)
            self.stkChart.dateTick.set_visible(False)
            self.stkChart.fig.canvas.draw()