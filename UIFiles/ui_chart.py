# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Chart(object):
    def setupUi(self, Chart):
        if not Chart.objectName():
            Chart.setObjectName(u"Chart")
        Chart.resize(951, 478)
        self.centralwidget = QWidget(Chart)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frmNav = QFrame(self.centralwidget)
        self.frmNav.setObjectName(u"frmNav")
        self.frmNav.setMaximumSize(QSize(250, 16777215))
        self.frmNav.setFrameShape(QFrame.StyledPanel)
        self.frmNav.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frmNav)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lblTimeFrame = QLabel(self.frame_3)
        self.lblTimeFrame.setObjectName(u"lblTimeFrame")
        self.lblTimeFrame.setGeometry(QRect(10, 20, 81, 20))
        self.cmbTimeFrame = QComboBox(self.frame_3)
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.setObjectName(u"cmbTimeFrame")
        self.cmbTimeFrame.setGeometry(QRect(100, 20, 101, 28))
        self.lblIndicators = QLabel(self.frame_3)
        self.lblIndicators.setObjectName(u"lblIndicators")
        self.lblIndicators.setGeometry(QRect(220, 20, 71, 20))
        self.cmbIndicators = QComboBox(self.frame_3)
        self.cmbIndicators.addItem("")
        self.cmbIndicators.addItem("")
        self.cmbIndicators.addItem("")
        self.cmbIndicators.addItem("")
        self.cmbIndicators.setObjectName(u"cmbIndicators")
        self.cmbIndicators.setGeometry(QRect(290, 20, 211, 28))
        self.lblIndicatorsAdded = QLabel(self.frame_3)
        self.lblIndicatorsAdded.setObjectName(u"lblIndicatorsAdded")
        self.lblIndicatorsAdded.setGeometry(QRect(532, 20, 121, 20))
        self.cmbIndicatorsAdded = QComboBox(self.frame_3)
        self.cmbIndicatorsAdded.setObjectName(u"cmbIndicatorsAdded")
        self.cmbIndicatorsAdded.setGeometry(QRect(660, 20, 191, 28))

        self.verticalLayout.addWidget(self.frame_3)

        self.frmCandleDetails = QFrame(self.frame_2)
        self.frmCandleDetails.setObjectName(u"frmCandleDetails")
        self.frmCandleDetails.setMinimumSize(QSize(0, 50))
        self.frmCandleDetails.setMaximumSize(QSize(16777215, 40))
        self.frmCandleDetails.setFrameShape(QFrame.StyledPanel)
        self.frmCandleDetails.setFrameShadow(QFrame.Raised)
        self.Gridlayout = QGridLayout(self.frmCandleDetails)
        self.Gridlayout.setObjectName(u"Gridlayout")
        self.lblClose = QLabel(self.frmCandleDetails)
        self.lblClose.setObjectName(u"lblClose")
        self.lblClose.setMaximumSize(QSize(20, 16777215))
        self.lblClose.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblClose, 0, 7, 1, 1)

        self.lblOpenVal = QLabel(self.frmCandleDetails)
        self.lblOpenVal.setObjectName(u"lblOpenVal")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOpenVal.sizePolicy().hasHeightForWidth())
        self.lblOpenVal.setSizePolicy(sizePolicy)

        self.Gridlayout.addWidget(self.lblOpenVal, 0, 2, 1, 1)

        self.lblLow = QLabel(self.frmCandleDetails)
        self.lblLow.setObjectName(u"lblLow")
        self.lblLow.setMaximumSize(QSize(20, 16777215))
        self.lblLow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblLow, 0, 5, 1, 1)

        self.lblHigh = QLabel(self.frmCandleDetails)
        self.lblHigh.setObjectName(u"lblHigh")
        self.lblHigh.setMaximumSize(QSize(20, 16777215))
        self.lblHigh.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblHigh, 0, 3, 1, 1)

        self.lblStkName = QLabel(self.frmCandleDetails)
        self.lblStkName.setObjectName(u"lblStkName")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblStkName.setFont(font)

        self.Gridlayout.addWidget(self.lblStkName, 0, 0, 1, 1)

        self.lblHighVal = QLabel(self.frmCandleDetails)
        self.lblHighVal.setObjectName(u"lblHighVal")
        sizePolicy.setHeightForWidth(self.lblHighVal.sizePolicy().hasHeightForWidth())
        self.lblHighVal.setSizePolicy(sizePolicy)

        self.Gridlayout.addWidget(self.lblHighVal, 0, 4, 1, 1)

        self.lblOpen = QLabel(self.frmCandleDetails)
        self.lblOpen.setObjectName(u"lblOpen")
        self.lblOpen.setMinimumSize(QSize(25, 0))
        self.lblOpen.setMaximumSize(QSize(25, 16777215))
        self.lblOpen.setLayoutDirection(Qt.LeftToRight)
        self.lblOpen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblOpen, 0, 1, 1, 1)

        self.lblLowVal = QLabel(self.frmCandleDetails)
        self.lblLowVal.setObjectName(u"lblLowVal")
        sizePolicy.setHeightForWidth(self.lblLowVal.sizePolicy().hasHeightForWidth())
        self.lblLowVal.setSizePolicy(sizePolicy)

        self.Gridlayout.addWidget(self.lblLowVal, 0, 6, 1, 1)

        self.lblCloseVal = QLabel(self.frmCandleDetails)
        self.lblCloseVal.setObjectName(u"lblCloseVal")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblCloseVal.sizePolicy().hasHeightForWidth())
        self.lblCloseVal.setSizePolicy(sizePolicy1)

        self.Gridlayout.addWidget(self.lblCloseVal, 0, 8, 1, 1)


        self.verticalLayout.addWidget(self.frmCandleDetails)

        self.frmChart = QFrame(self.frame_2)
        self.frmChart.setObjectName(u"frmChart")
        self.frmChart.setFrameShape(QFrame.StyledPanel)
        self.frmChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frmChart)


        self.horizontalLayout.addWidget(self.frame_2)

        Chart.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Chart)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 951, 25))
        Chart.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Chart)
        self.statusbar.setObjectName(u"statusbar")
        Chart.setStatusBar(self.statusbar)

        self.retranslateUi(Chart)

        self.cmbTimeFrame.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(Chart)
    # setupUi

    def retranslateUi(self, Chart):
        Chart.setWindowTitle(QCoreApplication.translate("Chart", u"MainWindow", None))
        self.lblTimeFrame.setText(QCoreApplication.translate("Chart", u"Time Frame", None))
        self.cmbTimeFrame.setItemText(0, QCoreApplication.translate("Chart", u"1 minute", None))
        self.cmbTimeFrame.setItemText(1, QCoreApplication.translate("Chart", u"2 minute", None))
        self.cmbTimeFrame.setItemText(2, QCoreApplication.translate("Chart", u"5 minute", None))
        self.cmbTimeFrame.setItemText(3, QCoreApplication.translate("Chart", u"15 minute", None))
        self.cmbTimeFrame.setItemText(4, QCoreApplication.translate("Chart", u"30 minute", None))
        self.cmbTimeFrame.setItemText(5, QCoreApplication.translate("Chart", u"60 minute", None))
        self.cmbTimeFrame.setItemText(6, QCoreApplication.translate("Chart", u"90 minute", None))
        self.cmbTimeFrame.setItemText(7, QCoreApplication.translate("Chart", u"1 day", None))
        self.cmbTimeFrame.setItemText(8, QCoreApplication.translate("Chart", u"5 day", None))
        self.cmbTimeFrame.setItemText(9, QCoreApplication.translate("Chart", u"1 week", None))
        self.cmbTimeFrame.setItemText(10, QCoreApplication.translate("Chart", u"1 month", None))
        self.cmbTimeFrame.setItemText(11, QCoreApplication.translate("Chart", u"3 month", None))

        self.lblIndicators.setText(QCoreApplication.translate("Chart", u"Indicators", None))
        self.cmbIndicators.setItemText(0, QCoreApplication.translate("Chart", u"None", None))
        self.cmbIndicators.setItemText(1, QCoreApplication.translate("Chart", u"Exponential Moving Average", None))
        self.cmbIndicators.setItemText(2, QCoreApplication.translate("Chart", u"Hull Moving Average", None))
        self.cmbIndicators.setItemText(3, QCoreApplication.translate("Chart", u"RSI", None))

        self.lblIndicatorsAdded.setText(QCoreApplication.translate("Chart", u"Indicators Added", None))
        self.lblClose.setText(QCoreApplication.translate("Chart", u"C", None))
        self.lblOpenVal.setText(QCoreApplication.translate("Chart", u"0.0", None))
        self.lblLow.setText(QCoreApplication.translate("Chart", u"L", None))
        self.lblHigh.setText(QCoreApplication.translate("Chart", u"H", None))
        self.lblStkName.setText(QCoreApplication.translate("Chart", u"stkName", None))
        self.lblHighVal.setText(QCoreApplication.translate("Chart", u"0.0", None))
        self.lblOpen.setText(QCoreApplication.translate("Chart", u"O", None))
        self.lblLowVal.setText(QCoreApplication.translate("Chart", u"0.0", None))
        self.lblCloseVal.setText(QCoreApplication.translate("Chart", u"0.0", None))
    # retranslateUi

