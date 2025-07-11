# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myOrders.ui'
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
    QLabel, QListView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_myOrders(object):
    def setupUi(self, myOrders):
        if not myOrders.objectName():
            myOrders.setObjectName(u"myOrders")
        myOrders.resize(1089, 578)
        myOrders.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.centralwidget = QWidget(myOrders)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.myOrdersTabWidget = QTabWidget(self.frame)
        self.myOrdersTabWidget.setObjectName(u"myOrdersTabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myOrdersTabWidget.sizePolicy().hasHeightForWidth())
        self.myOrdersTabWidget.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.myOrdersTabWidget.setFont(font1)
        self.myOrdersTabWidget.setStyleSheet(u"QWidget{\n"
"	border-radius : 5px;\n"
"	background-color: rgb(239, 239, 239);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QWidget::selection{\n"
"	color: rgb(170, 255, 127);\n"
"}")
        self.myOrdersTabWidget.setTabPosition(QTabWidget.North)
        self.myOrdersTabWidget.setTabShape(QTabWidget.Rounded)
        self.allOrdersWidget = QWidget()
        self.allOrdersWidget.setObjectName(u"allOrdersWidget")
        self.gridLayout_2 = QGridLayout(self.allOrdersWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblNoOrders = QLabel(self.allOrdersWidget)
        self.lblNoOrders.setObjectName(u"lblNoOrders")
        self.lblNoOrders.setMaximumSize(QSize(16777215, 16777215))
        self.lblNoOrders.setFont(font1)
        self.lblNoOrders.setStyleSheet(u"QLabel{\n"
"	padding-top: 20px;\n"
"}")
        self.lblNoOrders.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.lblNoOrders, 0, 0, 1, 1)

        self.lsvAllOrders = QListView(self.allOrdersWidget)
        self.lsvAllOrders.setObjectName(u"lsvAllOrders")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lsvAllOrders.setFont(font2)
        self.lsvAllOrders.setStyleSheet(u"QListView{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border : 2px solid black;\n"
"	border-radius : 5px;\n"
"}")
        self.lsvAllOrders.setAlternatingRowColors(True)
        self.lsvAllOrders.setResizeMode(QListView.Adjust)
        self.lsvAllOrders.setSpacing(0)

        self.gridLayout_2.addWidget(self.lsvAllOrders, 1, 0, 1, 1)

        self.myOrdersTabWidget.addTab(self.allOrdersWidget, "")
        self.pendingOrdersWidget = QWidget()
        self.pendingOrdersWidget.setObjectName(u"pendingOrdersWidget")
        self.gridLayout = QGridLayout(self.pendingOrdersWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblNoPendingOrders = QLabel(self.pendingOrdersWidget)
        self.lblNoPendingOrders.setObjectName(u"lblNoPendingOrders")
        self.lblNoPendingOrders.setMinimumSize(QSize(0, 0))
        self.lblNoPendingOrders.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.lblNoPendingOrders.setFont(font3)
        self.lblNoPendingOrders.setStyleSheet(u"QLabel{\n"
"	padding-top: 20px;\n"
"}")
        self.lblNoPendingOrders.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.lblNoPendingOrders, 0, 0, 1, 1)

        self.lsvPendingOrders = QListView(self.pendingOrdersWidget)
        self.lsvPendingOrders.setObjectName(u"lsvPendingOrders")
        self.lsvPendingOrders.setFont(font2)
        self.lsvPendingOrders.setStyleSheet(u"QListView{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border : 2px solid black;\n"
"	border-radius : 2px;\n"
"}")
        self.lsvPendingOrders.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.lsvPendingOrders, 1, 0, 1, 1)

        self.myOrdersTabWidget.addTab(self.pendingOrdersWidget, "")

        self.horizontalLayout.addWidget(self.myOrdersTabWidget)


        self.verticalLayout.addWidget(self.frame)

        myOrders.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(myOrders)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1089, 25))
        myOrders.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(myOrders)
        self.statusbar.setObjectName(u"statusbar")
        myOrders.setStatusBar(self.statusbar)

        self.retranslateUi(myOrders)

        self.myOrdersTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(myOrders)
    # setupUi

    def retranslateUi(self, myOrders):
        myOrders.setWindowTitle(QCoreApplication.translate("myOrders", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("myOrders", u"My Orders", None))
        self.lblNoOrders.setText(QCoreApplication.translate("myOrders", u"No Data", None))
        self.myOrdersTabWidget.setTabText(self.myOrdersTabWidget.indexOf(self.allOrdersWidget), QCoreApplication.translate("myOrders", u"ALL Orders", None))
        self.lblNoPendingOrders.setText(QCoreApplication.translate("myOrders", u"No Data", None))
        self.myOrdersTabWidget.setTabText(self.myOrdersTabWidget.indexOf(self.pendingOrdersWidget), QCoreApplication.translate("myOrders", u"Open Orders", None))
    # retranslateUi

