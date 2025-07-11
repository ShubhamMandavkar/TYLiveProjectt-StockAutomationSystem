# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Chart(object):
    def setupUi(self, Chart):
        if not Chart.objectName():
            Chart.setObjectName(u"Chart")
        Chart.resize(988, 527)
        self.centralwidget = QWidget(Chart)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lblTimeFrame = QLabel(self.frame)
        self.lblTimeFrame.setObjectName(u"lblTimeFrame")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lblTimeFrame.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblTimeFrame)

        self.cmbTimeFrame = QComboBox(self.frame)
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
        self.cmbTimeFrame.setMinimumSize(QSize(200, 35))
        self.cmbTimeFrame.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.cmbTimeFrame.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbTimeFrame)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(500, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblIndicators = QLabel(self.frame_4)
        self.lblIndicators.setObjectName(u"lblIndicators")
        self.lblIndicators.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblIndicators)

        self.cmbIndicators = QComboBox(self.frame_4)
        self.cmbIndicators.addItem("")
        self.cmbIndicators.addItem("")
        self.cmbIndicators.addItem("")
        self.cmbIndicators.setObjectName(u"cmbIndicators")
        self.cmbIndicators.setMinimumSize(QSize(250, 35))
        self.cmbIndicators.setMaximumSize(QSize(250, 16777215))
        self.cmbIndicators.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cmbIndicators)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

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
        self.lblClose.setFont(font)
        self.lblClose.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblClose, 0, 7, 1, 1)

        self.lblOpenVal = QLabel(self.frmCandleDetails)
        self.lblOpenVal.setObjectName(u"lblOpenVal")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOpenVal.sizePolicy().hasHeightForWidth())
        self.lblOpenVal.setSizePolicy(sizePolicy)
        self.lblOpenVal.setFont(font1)

        self.Gridlayout.addWidget(self.lblOpenVal, 0, 2, 1, 1)

        self.lblLow = QLabel(self.frmCandleDetails)
        self.lblLow.setObjectName(u"lblLow")
        self.lblLow.setMaximumSize(QSize(20, 16777215))
        self.lblLow.setFont(font)
        self.lblLow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblLow, 0, 5, 1, 1)

        self.lblHigh = QLabel(self.frmCandleDetails)
        self.lblHigh.setObjectName(u"lblHigh")
        self.lblHigh.setMaximumSize(QSize(20, 16777215))
        self.lblHigh.setFont(font)
        self.lblHigh.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblHigh, 0, 3, 1, 1)

        self.lblStkName = QLabel(self.frmCandleDetails)
        self.lblStkName.setObjectName(u"lblStkName")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lblStkName.setFont(font2)

        self.Gridlayout.addWidget(self.lblStkName, 0, 0, 1, 1)

        self.lblHighVal = QLabel(self.frmCandleDetails)
        self.lblHighVal.setObjectName(u"lblHighVal")
        sizePolicy.setHeightForWidth(self.lblHighVal.sizePolicy().hasHeightForWidth())
        self.lblHighVal.setSizePolicy(sizePolicy)
        self.lblHighVal.setFont(font1)

        self.Gridlayout.addWidget(self.lblHighVal, 0, 4, 1, 1)

        self.lblOpen = QLabel(self.frmCandleDetails)
        self.lblOpen.setObjectName(u"lblOpen")
        self.lblOpen.setMinimumSize(QSize(25, 0))
        self.lblOpen.setMaximumSize(QSize(25, 16777215))
        self.lblOpen.setFont(font)
        self.lblOpen.setLayoutDirection(Qt.LeftToRight)
        self.lblOpen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.Gridlayout.addWidget(self.lblOpen, 0, 1, 1, 1)

        self.lblLowVal = QLabel(self.frmCandleDetails)
        self.lblLowVal.setObjectName(u"lblLowVal")
        sizePolicy.setHeightForWidth(self.lblLowVal.sizePolicy().hasHeightForWidth())
        self.lblLowVal.setSizePolicy(sizePolicy)
        self.lblLowVal.setFont(font1)

        self.Gridlayout.addWidget(self.lblLowVal, 0, 6, 1, 1)

        self.lblCloseVal = QLabel(self.frmCandleDetails)
        self.lblCloseVal.setObjectName(u"lblCloseVal")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblCloseVal.sizePolicy().hasHeightForWidth())
        self.lblCloseVal.setSizePolicy(sizePolicy1)
        self.lblCloseVal.setFont(font1)

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
        self.menubar.setGeometry(QRect(0, 0, 988, 25))
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

