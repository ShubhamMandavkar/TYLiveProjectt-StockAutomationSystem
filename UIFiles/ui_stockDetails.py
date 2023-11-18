# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockDetails.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_stockDetails(object):
    def setupUi(self, stockDetails):
        if not stockDetails.objectName():
            stockDetails.setObjectName(u"stockDetails")
        stockDetails.resize(956, 600)
        self.centralwidget = QWidget(stockDetails)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblStkName = QLabel(self.frame_5)
        self.lblStkName.setObjectName(u"lblStkName")

        self.horizontalLayout_2.addWidget(self.lblStkName)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblSymbol = QLabel(self.frame_6)
        self.lblSymbol.setObjectName(u"lblSymbol")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblSymbol)

        self.lblSymbolVal = QLabel(self.frame_6)
        self.lblSymbolVal.setObjectName(u"lblSymbolVal")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lblSymbolVal)

        self.lblCompany = QLabel(self.frame_6)
        self.lblCompany.setObjectName(u"lblCompany")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblCompany)

        self.lblCompanyVal = QLabel(self.frame_6)
        self.lblCompanyVal.setObjectName(u"lblCompanyVal")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lblCompanyVal)

        self.lblExchange = QLabel(self.frame_6)
        self.lblExchange.setObjectName(u"lblExchange")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lblExchange)

        self.lblOpen = QLabel(self.frame_6)
        self.lblOpen.setObjectName(u"lblOpen")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lblOpen)

        self.lblOpenVal = QLabel(self.frame_6)
        self.lblOpenVal.setObjectName(u"lblOpenVal")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lblOpenVal)

        self.lblHigh = QLabel(self.frame_6)
        self.lblHigh.setObjectName(u"lblHigh")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lblHigh)

        self.lblHighVal = QLabel(self.frame_6)
        self.lblHighVal.setObjectName(u"lblHighVal")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lblHighVal)

        self.lblLow = QLabel(self.frame_6)
        self.lblLow.setObjectName(u"lblLow")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lblLow)

        self.lblLowVal = QLabel(self.frame_6)
        self.lblLowVal.setObjectName(u"lblLowVal")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lblLowVal)

        self.lblClose = QLabel(self.frame_6)
        self.lblClose.setObjectName(u"lblClose")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lblClose)

        self.lblCloseVal = QLabel(self.frame_6)
        self.lblCloseVal.setObjectName(u"lblCloseVal")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lblCloseVal)

        self.lblChange = QLabel(self.frame_6)
        self.lblChange.setObjectName(u"lblChange")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lblChange)

        self.lblChangeVal = QLabel(self.frame_6)
        self.lblChangeVal.setObjectName(u"lblChangeVal")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.lblChangeVal)

        self.lbl52wkHigh = QLabel(self.frame_6)
        self.lbl52wkHigh.setObjectName(u"lbl52wkHigh")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lbl52wkHigh)

        self.lbl52wkHighVal = QLabel(self.frame_6)
        self.lbl52wkHighVal.setObjectName(u"lbl52wkHighVal")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.lbl52wkHighVal)

        self.lbl52wkLow = QLabel(self.frame_6)
        self.lbl52wkLow.setObjectName(u"lbl52wkLow")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.lbl52wkLow)

        self.lbl52wkLowVal = QLabel(self.frame_6)
        self.lbl52wkLowVal.setObjectName(u"lbl52wkLowVal")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.lbl52wkLowVal)

        self.lblVolume = QLabel(self.frame_6)
        self.lblVolume.setObjectName(u"lblVolume")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.lblVolume)

        self.lblVolumeVal = QLabel(self.frame_6)
        self.lblVolumeVal.setObjectName(u"lblVolumeVal")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.lblVolumeVal)

        self.lblExchangeVal = QLabel(self.frame_6)
        self.lblExchangeVal.setObjectName(u"lblExchangeVal")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lblExchangeVal)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnAlert = QPushButton(self.frame_7)
        self.btnAlert.setObjectName(u"btnAlert")

        self.horizontalLayout_3.addWidget(self.btnAlert)

        self.btnChart = QPushButton(self.frame_7)
        self.btnChart.setObjectName(u"btnChart")

        self.horizontalLayout_3.addWidget(self.btnChart)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)

        stockDetails.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(stockDetails)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 956, 25))
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
        self.lblSymbol.setText(QCoreApplication.translate("stockDetails", u"Symbol : ", None))
        self.lblSymbolVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblCompany.setText(QCoreApplication.translate("stockDetails", u"Company Name :", None))
        self.lblCompanyVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblExchange.setText(QCoreApplication.translate("stockDetails", u"Exchange : ", None))
        self.lblOpen.setText(QCoreApplication.translate("stockDetails", u"Open : ", None))
        self.lblOpenVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblHigh.setText(QCoreApplication.translate("stockDetails", u"High : ", None))
        self.lblHighVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblLow.setText(QCoreApplication.translate("stockDetails", u"Low : ", None))
        self.lblLowVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblClose.setText(QCoreApplication.translate("stockDetails", u"Close : ", None))
        self.lblCloseVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblChange.setText(QCoreApplication.translate("stockDetails", u"Change : ", None))
        self.lblChangeVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lbl52wkHigh.setText(QCoreApplication.translate("stockDetails", u"52 Week High : ", None))
        self.lbl52wkHighVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lbl52wkLow.setText(QCoreApplication.translate("stockDetails", u"52 Week Low : ", None))
        self.lbl52wkLowVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblVolume.setText(QCoreApplication.translate("stockDetails", u"Volume : ", None))
        self.lblVolumeVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.lblExchangeVal.setText(QCoreApplication.translate("stockDetails", u"TextLabel", None))
        self.btnAlert.setText(QCoreApplication.translate("stockDetails", u"Add Alert", None))
        self.btnChart.setText(QCoreApplication.translate("stockDetails", u"Chart", None))
    # retranslateUi

