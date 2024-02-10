# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1113, 567)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frmNavBar = QFrame(self.centralwidget)
        self.frmNavBar.setObjectName(u"frmNavBar")
        self.frmNavBar.setMaximumSize(QSize(250, 16777215))
        self.frmNavBar.setFrameShape(QFrame.StyledPanel)
        self.frmNavBar.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frmNavBar)
        self.formLayout.setObjectName(u"formLayout")
        self.btnHome = QPushButton(self.frmNavBar)
        self.btnHome.setObjectName(u"btnHome")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnHome.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btnHome)

        self.btnMyAlerts = QPushButton(self.frmNavBar)
        self.btnMyAlerts.setObjectName(u"btnMyAlerts")
        self.btnMyAlerts.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btnMyAlerts)

        self.btnHoldings = QPushButton(self.frmNavBar)
        self.btnHoldings.setObjectName(u"btnHoldings")
        self.btnHoldings.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.btnHoldings)

        self.btnWatchlists = QPushButton(self.frmNavBar)
        self.btnWatchlists.setObjectName(u"btnWatchlists")
        self.btnWatchlists.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.btnWatchlists)

        self.btnMyOrders = QPushButton(self.frmNavBar)
        self.btnMyOrders.setObjectName(u"btnMyOrders")
        self.btnMyOrders.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btnMyOrders)

        self.btnCustomDetails = QPushButton(self.frmNavBar)
        self.btnCustomDetails.setObjectName(u"btnCustomDetails")
        self.btnCustomDetails.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.btnCustomDetails)

        self.btnSpecialAlerts = QPushButton(self.frmNavBar)
        self.btnSpecialAlerts.setObjectName(u"btnSpecialAlerts")
        self.btnSpecialAlerts.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btnSpecialAlerts)


        self.horizontalLayout.addWidget(self.frmNavBar)

        self.frmContent = QFrame(self.centralwidget)
        self.frmContent.setObjectName(u"frmContent")
        self.frmContent.setFrameShape(QFrame.StyledPanel)
        self.frmContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frmContent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frmContent)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnSearch = QPushButton(self.frame)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(580, 30, 141, 41))
        self.btnSearch.setFont(font)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frmContent)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblOrders = QLabel(self.frame_2)
        self.lblOrders.setObjectName(u"lblOrders")
        self.lblOrders.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lblOrders.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.lblOrders)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(600, 70))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblClosed = QLabel(self.frame_3)
        self.lblClosed.setObjectName(u"lblClosed")
        self.lblClosed.setFont(font)
        self.lblClosed.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblClosed, 2, 1, 1, 1)

        self.lblRejected = QLabel(self.frame_3)
        self.lblRejected.setObjectName(u"lblRejected")
        self.lblRejected.setFont(font)
        self.lblRejected.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblRejected, 2, 2, 1, 1)

        self.lblPendingsVal = QLabel(self.frame_3)
        self.lblPendingsVal.setObjectName(u"lblPendingsVal")
        self.lblPendingsVal.setFont(font)
        self.lblPendingsVal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblPendingsVal, 0, 0, 1, 1)

        self.lblRejectedVal = QLabel(self.frame_3)
        self.lblRejectedVal.setObjectName(u"lblRejectedVal")
        self.lblRejectedVal.setFont(font)
        self.lblRejectedVal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblRejectedVal, 0, 2, 1, 1)

        self.lblClosedVal = QLabel(self.frame_3)
        self.lblClosedVal.setObjectName(u"lblClosedVal")
        self.lblClosedVal.setFont(font)
        self.lblClosedVal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblClosedVal, 0, 1, 1, 1)

        self.lblPendings = QLabel(self.frame_3)
        self.lblPendings.setObjectName(u"lblPendings")
        self.lblPendings.setFont(font)
        self.lblPendings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblPendings, 2, 0, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.frame_3)

        self.lblHoldings = QLabel(self.frame_2)
        self.lblHoldings.setObjectName(u"lblHoldings")
        self.lblHoldings.setMaximumSize(QSize(16777215, 40))
        self.lblHoldings.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.lblHoldings)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(600, 70))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblToltalInv = QLabel(self.frame_5)
        self.lblToltalInv.setObjectName(u"lblToltalInv")
        self.lblToltalInv.setFont(font)
        self.lblToltalInv.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblToltalInv, 1, 0, 1, 1)

        self.lbalCurrentValueVal = QLabel(self.frame_5)
        self.lbalCurrentValueVal.setObjectName(u"lbalCurrentValueVal")
        self.lbalCurrentValueVal.setFont(font)
        self.lbalCurrentValueVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbalCurrentValueVal, 0, 1, 1, 1)

        self.lblPandLVal = QLabel(self.frame_5)
        self.lblPandLVal.setObjectName(u"lblPandLVal")
        self.lblPandLVal.setFont(font)
        self.lblPandLVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblPandLVal, 0, 2, 1, 1)

        self.lblTotalInvVal = QLabel(self.frame_5)
        self.lblTotalInvVal.setObjectName(u"lblTotalInvVal")
        self.lblTotalInvVal.setFont(font)
        self.lblTotalInvVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTotalInvVal, 0, 0, 1, 1)

        self.lblPandL = QLabel(self.frame_5)
        self.lblPandL.setObjectName(u"lblPandL")
        self.lblPandL.setFont(font)
        self.lblPandL.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblPandL, 1, 2, 1, 1)

        self.lblCurrentValue = QLabel(self.frame_5)
        self.lblCurrentValue.setObjectName(u"lblCurrentValue")
        self.lblCurrentValue.setFont(font)
        self.lblCurrentValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblCurrentValue, 1, 1, 1, 1)


        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frmContent)

        Home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1113, 25))
        Home.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Home)
        self.statusbar.setObjectName(u"statusbar")
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"MainWindow", None))
        self.btnHome.setText(QCoreApplication.translate("Home", u"Home", None))
        self.btnMyAlerts.setText(QCoreApplication.translate("Home", u"MyAlerts", None))
        self.btnHoldings.setText(QCoreApplication.translate("Home", u"Holdings", None))
        self.btnWatchlists.setText(QCoreApplication.translate("Home", u"Watchlists", None))
        self.btnMyOrders.setText(QCoreApplication.translate("Home", u"MyOrders", None))
        self.btnCustomDetails.setText(QCoreApplication.translate("Home", u"CustomDetails", None))
        self.btnSpecialAlerts.setText(QCoreApplication.translate("Home", u"SpecialAlerts", None))
        self.btnSearch.setText(QCoreApplication.translate("Home", u"Search", None))
        self.lblOrders.setText(QCoreApplication.translate("Home", u"Orders", None))
        self.lblClosed.setText(QCoreApplication.translate("Home", u"Closed", None))
        self.lblRejected.setText(QCoreApplication.translate("Home", u"Rejected", None))
        self.lblPendingsVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblRejectedVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblClosedVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblPendings.setText(QCoreApplication.translate("Home", u"Pendings", None))
        self.lblHoldings.setText(QCoreApplication.translate("Home", u"Holdings", None))
        self.lblToltalInv.setText(QCoreApplication.translate("Home", u"Total Investment", None))
        self.lbalCurrentValueVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblPandLVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblTotalInvVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblPandL.setText(QCoreApplication.translate("Home", u"P & L", None))
        self.lblCurrentValue.setText(QCoreApplication.translate("Home", u"Current Value", None))
    # retranslateUi

