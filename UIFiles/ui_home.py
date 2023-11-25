# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1156, 604)
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
        self.btnMyAlerts = QPushButton(self.frmNavBar)
        self.btnMyAlerts.setObjectName(u"btnMyAlerts")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btnMyAlerts)

        self.btnHoldings = QPushButton(self.frmNavBar)
        self.btnHoldings.setObjectName(u"btnHoldings")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btnHoldings)

        self.btnCustomDetails = QPushButton(self.frmNavBar)
        self.btnCustomDetails.setObjectName(u"btnCustomDetails")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.btnCustomDetails)

        self.btnWatchlists = QPushButton(self.frmNavBar)
        self.btnWatchlists.setObjectName(u"btnWatchlists")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btnWatchlists)

        self.btnHome = QPushButton(self.frmNavBar)
        self.btnHome.setObjectName(u"btnHome")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btnHome)


        self.horizontalLayout.addWidget(self.frmNavBar)

        self.frmContent = QFrame(self.centralwidget)
        self.frmContent.setObjectName(u"frmContent")
        self.frmContent.setFrameShape(QFrame.StyledPanel)
        self.frmContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frmContent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frmContent)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnSearch = QPushButton(self.frame)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(490, 40, 141, 29))

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frmContent)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblOrders = QLabel(self.frame_2)
        self.lblOrders.setObjectName(u"lblOrders")
        self.lblOrders.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.lblOrders)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(600, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblClosed = QLabel(self.frame_3)
        self.lblClosed.setObjectName(u"lblClosed")
        self.lblClosed.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblClosed, 2, 1, 1, 1)

        self.lblPendings = QLabel(self.frame_3)
        self.lblPendings.setObjectName(u"lblPendings")
        self.lblPendings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblPendings, 2, 0, 1, 1)

        self.lblPendingsVal = QLabel(self.frame_3)
        self.lblPendingsVal.setObjectName(u"lblPendingsVal")
        self.lblPendingsVal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblPendingsVal, 0, 0, 1, 1)

        self.lblClosedVal = QLabel(self.frame_3)
        self.lblClosedVal.setObjectName(u"lblClosedVal")
        self.lblClosedVal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblClosedVal, 0, 1, 1, 1)

        self.lblRejectedVal = QLabel(self.frame_3)
        self.lblRejectedVal.setObjectName(u"lblRejectedVal")
        self.lblRejectedVal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblRejectedVal, 0, 2, 1, 1)

        self.lblRejected = QLabel(self.frame_3)
        self.lblRejected.setObjectName(u"lblRejected")
        self.lblRejected.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblRejected, 2, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.lblHoldings = QLabel(self.frame_2)
        self.lblHoldings.setObjectName(u"lblHoldings")
        self.lblHoldings.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.lblHoldings)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(600, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblToltalInv = QLabel(self.frame_5)
        self.lblToltalInv.setObjectName(u"lblToltalInv")
        self.lblToltalInv.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblToltalInv, 1, 0, 1, 1)

        self.lbalCurrentValueVal = QLabel(self.frame_5)
        self.lbalCurrentValueVal.setObjectName(u"lbalCurrentValueVal")
        self.lbalCurrentValueVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbalCurrentValueVal, 0, 1, 1, 1)

        self.lblPandLVal = QLabel(self.frame_5)
        self.lblPandLVal.setObjectName(u"lblPandLVal")
        self.lblPandLVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblPandLVal, 0, 2, 1, 1)

        self.lblTotalInvVal = QLabel(self.frame_5)
        self.lblTotalInvVal.setObjectName(u"lblTotalInvVal")
        self.lblTotalInvVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblTotalInvVal, 0, 0, 1, 1)

        self.lblPandL = QLabel(self.frame_5)
        self.lblPandL.setObjectName(u"lblPandL")
        self.lblPandL.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblPandL, 1, 2, 1, 1)

        self.lblCurrentValue = QLabel(self.frame_5)
        self.lblCurrentValue.setObjectName(u"lblCurrentValue")
        self.lblCurrentValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblCurrentValue, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.lblPositions = QLabel(self.frame_2)
        self.lblPositions.setObjectName(u"lblPositions")
        self.lblPositions.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.lblPositions)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(600, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblTotalPandL = QLabel(self.frame_4)
        self.lblTotalPandL.setObjectName(u"lblTotalPandL")
        self.lblTotalPandL.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblTotalPandL, 1, 1, 1, 1)

        self.lblTotalPandLVal = QLabel(self.frame_4)
        self.lblTotalPandLVal.setObjectName(u"lblTotalPandLVal")
        self.lblTotalPandLVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblTotalPandLVal, 0, 1, 1, 1)

        self.lblOpenPos = QLabel(self.frame_4)
        self.lblOpenPos.setObjectName(u"lblOpenPos")
        self.lblOpenPos.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblOpenPos, 1, 0, 1, 1)

        self.lblOpenPosVal = QLabel(self.frame_4)
        self.lblOpenPosVal.setObjectName(u"lblOpenPosVal")
        self.lblOpenPosVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblOpenPosVal, 0, 0, 1, 1)

        self.lblDayMTMVal = QLabel(self.frame_4)
        self.lblDayMTMVal.setObjectName(u"lblDayMTMVal")
        self.lblDayMTMVal.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblDayMTMVal, 0, 2, 1, 1)

        self.lblDayMTM = QLabel(self.frame_4)
        self.lblDayMTM.setObjectName(u"lblDayMTM")
        self.lblDayMTM.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblDayMTM, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frmContent)

        Home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1156, 25))
        Home.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Home)
        self.statusbar.setObjectName(u"statusbar")
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"MainWindow", None))
        self.btnMyAlerts.setText(QCoreApplication.translate("Home", u"MyAlerts", None))
        self.btnHoldings.setText(QCoreApplication.translate("Home", u"Holdings", None))
        self.btnCustomDetails.setText(QCoreApplication.translate("Home", u"CustomDetails", None))
        self.btnWatchlists.setText(QCoreApplication.translate("Home", u"Watchlists", None))
        self.btnHome.setText(QCoreApplication.translate("Home", u"Home", None))
        self.btnSearch.setText(QCoreApplication.translate("Home", u"Search", None))
        self.lblOrders.setText(QCoreApplication.translate("Home", u"Orders", None))
        self.lblClosed.setText(QCoreApplication.translate("Home", u"Closed", None))
        self.lblPendings.setText(QCoreApplication.translate("Home", u"Pendings", None))
        self.lblPendingsVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblClosedVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblRejectedVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblRejected.setText(QCoreApplication.translate("Home", u"Rejected", None))
        self.lblHoldings.setText(QCoreApplication.translate("Home", u"Holdings", None))
        self.lblToltalInv.setText(QCoreApplication.translate("Home", u"Total Investment", None))
        self.lbalCurrentValueVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblPandLVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblTotalInvVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblPandL.setText(QCoreApplication.translate("Home", u"P & L", None))
        self.lblCurrentValue.setText(QCoreApplication.translate("Home", u"Current Value", None))
        self.lblPositions.setText(QCoreApplication.translate("Home", u"Positions", None))
        self.lblTotalPandL.setText(QCoreApplication.translate("Home", u"Total P & L", None))
        self.lblTotalPandLVal.setText(QCoreApplication.translate("Home", u"0 ", None))
        self.lblOpenPos.setText(QCoreApplication.translate("Home", u"Open Positions", None))
        self.lblOpenPosVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblDayMTMVal.setText(QCoreApplication.translate("Home", u"0", None))
        self.lblDayMTM.setText(QCoreApplication.translate("Home", u"Day MTM", None))
    # retranslateUi

