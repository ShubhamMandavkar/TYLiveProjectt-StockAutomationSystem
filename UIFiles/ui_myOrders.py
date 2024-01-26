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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListView, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_myOrders(object):
    def setupUi(self, myOrders):
        if not myOrders.objectName():
            myOrders.setObjectName(u"myOrders")
        myOrders.resize(866, 507)
        self.centralwidget = QWidget(myOrders)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.myOrdersTabWidget = QTabWidget(self.frame)
        self.myOrdersTabWidget.setObjectName(u"myOrdersTabWidget")
        font1 = QFont()
        font1.setPointSize(9)
        self.myOrdersTabWidget.setFont(font1)
        self.allOrdersWidget = QWidget()
        self.allOrdersWidget.setObjectName(u"allOrdersWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.allOrdersWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lsvAllOrders = QListView(self.allOrdersWidget)
        self.lsvAllOrders.setObjectName(u"lsvAllOrders")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lsvAllOrders.setFont(font2)
        self.lsvAllOrders.setAlternatingRowColors(True)

        self.horizontalLayout_2.addWidget(self.lsvAllOrders)

        self.myOrdersTabWidget.addTab(self.allOrdersWidget, "")
        self.pendingOrdersWidget = QWidget()
        self.pendingOrdersWidget.setObjectName(u"pendingOrdersWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.pendingOrdersWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lsvPendingOrders = QListView(self.pendingOrdersWidget)
        self.lsvPendingOrders.setObjectName(u"lsvPendingOrders")
        self.lsvPendingOrders.setFont(font2)

        self.horizontalLayout_3.addWidget(self.lsvPendingOrders)

        self.myOrdersTabWidget.addTab(self.pendingOrdersWidget, "")

        self.horizontalLayout.addWidget(self.myOrdersTabWidget)


        self.verticalLayout.addWidget(self.frame)

        myOrders.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(myOrders)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 25))
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
        self.myOrdersTabWidget.setTabText(self.myOrdersTabWidget.indexOf(self.allOrdersWidget), QCoreApplication.translate("myOrders", u"ALL Orders", None))
        self.myOrdersTabWidget.setTabText(self.myOrdersTabWidget.indexOf(self.pendingOrdersWidget), QCoreApplication.translate("myOrders", u"Open Orders", None))
    # retranslateUi

