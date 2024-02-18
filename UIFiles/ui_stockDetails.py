# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockDetails.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_stockDetails(object):
    def setupUi(self, stockDetails):
        if not stockDetails.objectName():
            stockDetails.setObjectName(u"stockDetails")
        stockDetails.resize(894, 689)
        self.centralwidget = QWidget(stockDetails)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	\n"
"	border-radius : 15px;\n"
"	background-color: #DC143C;\n"
"	background-color: rgb(239, 22, 65);\n"
"background-color: white;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblStkName = QLabel(self.frame_5)
        self.lblStkName.setObjectName(u"lblStkName")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lblStkName.setFont(font)
        self.lblStkName.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lblStkName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblStkName)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setLayoutDirection(Qt.LeftToRight)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblSymbol = QLabel(self.frame_6)
        self.lblSymbol.setObjectName(u"lblSymbol")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSymbol.sizePolicy().hasHeightForWidth())
        self.lblSymbol.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblSymbol.setFont(font1)
        self.lblSymbol.setLayoutDirection(Qt.LeftToRight)
        self.lblSymbol.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblSymbol, 0, 0, 1, 1)

        self.lblSymbolVal = QLabel(self.frame_6)
        self.lblSymbolVal.setObjectName(u"lblSymbolVal")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lblSymbolVal.setFont(font2)

        self.gridLayout_2.addWidget(self.lblSymbolVal, 0, 1, 1, 1)

        self.lblCompany = QLabel(self.frame_6)
        self.lblCompany.setObjectName(u"lblCompany")
        self.lblCompany.setFont(font1)
        self.lblCompany.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblCompany, 1, 0, 1, 1)

        self.lblCompanyVal = QLabel(self.frame_6)
        self.lblCompanyVal.setObjectName(u"lblCompanyVal")
        font3 = QFont()
        font3.setPointSize(12)
        self.lblCompanyVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblCompanyVal, 1, 1, 1, 1)

        self.lblExchange = QLabel(self.frame_6)
        self.lblExchange.setObjectName(u"lblExchange")
        self.lblExchange.setFont(font1)
        self.lblExchange.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblExchange, 2, 0, 1, 1)

        self.lblExchangeVal = QLabel(self.frame_6)
        self.lblExchangeVal.setObjectName(u"lblExchangeVal")
        self.lblExchangeVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblExchangeVal, 2, 1, 1, 1)

        self.lblOpen = QLabel(self.frame_6)
        self.lblOpen.setObjectName(u"lblOpen")
        self.lblOpen.setFont(font1)
        self.lblOpen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblOpen, 3, 0, 1, 1)

        self.lblOpenVal = QLabel(self.frame_6)
        self.lblOpenVal.setObjectName(u"lblOpenVal")
        self.lblOpenVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblOpenVal, 3, 1, 1, 1)

        self.lblHigh = QLabel(self.frame_6)
        self.lblHigh.setObjectName(u"lblHigh")
        self.lblHigh.setFont(font1)
        self.lblHigh.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblHigh, 4, 0, 1, 1)

        self.lblHighVal = QLabel(self.frame_6)
        self.lblHighVal.setObjectName(u"lblHighVal")
        self.lblHighVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblHighVal, 4, 1, 1, 1)

        self.lblLow = QLabel(self.frame_6)
        self.lblLow.setObjectName(u"lblLow")
        self.lblLow.setFont(font1)
        self.lblLow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblLow, 5, 0, 1, 1)

        self.lblLowVal = QLabel(self.frame_6)
        self.lblLowVal.setObjectName(u"lblLowVal")
        self.lblLowVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblLowVal, 5, 1, 1, 1)

        self.lblClose = QLabel(self.frame_6)
        self.lblClose.setObjectName(u"lblClose")
        self.lblClose.setFont(font1)
        self.lblClose.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblClose, 6, 0, 1, 1)

        self.lblCloseVal = QLabel(self.frame_6)
        self.lblCloseVal.setObjectName(u"lblCloseVal")
        self.lblCloseVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblCloseVal, 6, 1, 1, 1)

        self.lblChange = QLabel(self.frame_6)
        self.lblChange.setObjectName(u"lblChange")
        self.lblChange.setFont(font1)
        self.lblChange.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblChange, 7, 0, 1, 1)

        self.lblChangeVal = QLabel(self.frame_6)
        self.lblChangeVal.setObjectName(u"lblChangeVal")
        self.lblChangeVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblChangeVal, 7, 1, 1, 1)

        self.lbl52wkHigh = QLabel(self.frame_6)
        self.lbl52wkHigh.setObjectName(u"lbl52wkHigh")
        self.lbl52wkHigh.setFont(font1)
        self.lbl52wkHigh.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl52wkHigh, 8, 0, 1, 1)

        self.lbl52wkHighVal = QLabel(self.frame_6)
        self.lbl52wkHighVal.setObjectName(u"lbl52wkHighVal")
        self.lbl52wkHighVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl52wkHighVal, 8, 1, 1, 1)

        self.lbl52wkLow = QLabel(self.frame_6)
        self.lbl52wkLow.setObjectName(u"lbl52wkLow")
        self.lbl52wkLow.setFont(font1)
        self.lbl52wkLow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl52wkLow, 9, 0, 1, 1)

        self.lbl52wkLowVal = QLabel(self.frame_6)
        self.lbl52wkLowVal.setObjectName(u"lbl52wkLowVal")
        self.lbl52wkLowVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lbl52wkLowVal, 9, 1, 1, 1)

        self.lblVolume = QLabel(self.frame_6)
        self.lblVolume.setObjectName(u"lblVolume")
        self.lblVolume.setFont(font1)
        self.lblVolume.setLayoutDirection(Qt.LeftToRight)
        self.lblVolume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lblVolume, 10, 0, 1, 1)

        self.lblVolumeVal = QLabel(self.frame_6)
        self.lblVolumeVal.setObjectName(u"lblVolumeVal")
        self.lblVolumeVal.setFont(font3)

        self.gridLayout_2.addWidget(self.lblVolumeVal, 10, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnChart = QPushButton(self.frame_7)
        self.btnChart.setObjectName(u"btnChart")
        self.btnChart.setMinimumSize(QSize(0, 45))
        self.btnChart.setMaximumSize(QSize(125, 16777215))
        self.btnChart.setFont(font1)
        self.btnChart.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.btnChart, 1, 3, 1, 1)

        self.btnBuy = QPushButton(self.frame_7)
        self.btnBuy.setObjectName(u"btnBuy")
        self.btnBuy.setMinimumSize(QSize(60, 45))
        self.btnBuy.setMaximumSize(QSize(125, 16777215))
        self.btnBuy.setFont(font1)
        self.btnBuy.setStyleSheet(u"QPushButton{\n"
"	background-color: #00aa33;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #0fff50;\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.btnBuy, 1, 0, 1, 1)

        self.btnSell = QPushButton(self.frame_7)
        self.btnSell.setObjectName(u"btnSell")
        self.btnSell.setMinimumSize(QSize(0, 45))
        self.btnSell.setMaximumSize(QSize(125, 16777215))
        self.btnSell.setFont(font1)
        self.btnSell.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(200, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #FF3131;\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.btnSell, 1, 1, 1, 1)

        self.btnAlert = QPushButton(self.frame_7)
        self.btnAlert.setObjectName(u"btnAlert")
        self.btnAlert.setMinimumSize(QSize(0, 45))
        self.btnAlert.setMaximumSize(QSize(125, 16777215))
        self.btnAlert.setFont(font1)
        self.btnAlert.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #29a788;\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.btnAlert, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_4)

        stockDetails.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(stockDetails)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 894, 25))
        stockDetails.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(stockDetails)
        self.statusbar.setObjectName(u"statusbar")
        stockDetails.setStatusBar(self.statusbar)

        self.retranslateUi(stockDetails)

        QMetaObject.connectSlotsByName(stockDetails)
    # setupUi

    def retranslateUi(self, stockDetails):
        stockDetails.setWindowTitle(QCoreApplication.translate("stockDetails", u"MainWindow", None))
        self.lblStkName.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblSymbol.setText(QCoreApplication.translate("stockDetails", u"Symbol :", None))
        self.lblSymbolVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblCompany.setText(QCoreApplication.translate("stockDetails", u"Company Name :", None))
        self.lblCompanyVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblExchange.setText(QCoreApplication.translate("stockDetails", u"Exchange : ", None))
        self.lblExchangeVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblOpen.setText(QCoreApplication.translate("stockDetails", u"Open : ", None))
        self.lblOpenVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblHigh.setText(QCoreApplication.translate("stockDetails", u"High : ", None))
        self.lblHighVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblLow.setText(QCoreApplication.translate("stockDetails", u"Low : ", None))
        self.lblLowVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblClose.setText(QCoreApplication.translate("stockDetails", u"Close : ", None))
        self.lblCloseVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblChange.setText(QCoreApplication.translate("stockDetails", u"Change : ", None))
        self.lblChangeVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lbl52wkHigh.setText(QCoreApplication.translate("stockDetails", u"52 Week High : ", None))
        self.lbl52wkHighVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lbl52wkLow.setText(QCoreApplication.translate("stockDetails", u"52 Week Low : ", None))
        self.lbl52wkLowVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.lblVolume.setText(QCoreApplication.translate("stockDetails", u"Volume : ", None))
        self.lblVolumeVal.setText(QCoreApplication.translate("stockDetails", u"?", None))
        self.btnChart.setText(QCoreApplication.translate("stockDetails", u"Chart", None))
        self.btnBuy.setText(QCoreApplication.translate("stockDetails", u"Buy", None))
        self.btnSell.setText(QCoreApplication.translate("stockDetails", u"Sell", None))
        self.btnAlert.setText(QCoreApplication.translate("stockDetails", u"Add Alert", None))
    # retranslateUi

