# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myAlerts.ui'
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
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_myAlerts(object):
    def setupUi(self, myAlerts):
        if not myAlerts.objectName():
            myAlerts.setObjectName(u"myAlerts")
        myAlerts.resize(1140, 605)
        self.centralwidget = QWidget(myAlerts)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frmNavBar = QFrame(self.centralwidget)
        self.frmNavBar.setObjectName(u"frmNavBar")
        self.frmNavBar.setMinimumSize(QSize(250, 0))
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

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
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
        self.lsvMyAlerts = QListView(self.frame_4)
        self.lsvMyAlerts.setObjectName(u"lsvMyAlerts")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lsvMyAlerts.setFont(font)
        self.lsvMyAlerts.setProperty("isWrapping", False)
        self.lsvMyAlerts.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lsvMyAlerts)

        self.btnDelete = QPushButton(self.frame_4)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)

        myAlerts.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(myAlerts)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1140, 25))
        myAlerts.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(myAlerts)
        self.statusbar.setObjectName(u"statusbar")
        myAlerts.setStatusBar(self.statusbar)

        self.retranslateUi(myAlerts)

        QMetaObject.connectSlotsByName(myAlerts)
    # setupUi

    def retranslateUi(self, myAlerts):
        myAlerts.setWindowTitle(QCoreApplication.translate("myAlerts", u"MainWindow", None))
        self.btnMyAlerts.setText(QCoreApplication.translate("myAlerts", u"MyAlerts", None))
        self.btnHoldings.setText(QCoreApplication.translate("myAlerts", u"Holdings", None))
        self.btnCustomDetails.setText(QCoreApplication.translate("myAlerts", u"CustomDetails", None))
        self.btnWatchlists.setText(QCoreApplication.translate("myAlerts", u"Watchlists", None))
        self.btnHome.setText(QCoreApplication.translate("myAlerts", u"Home", None))
        self.btnDelete.setText(QCoreApplication.translate("myAlerts", u"Delete", None))
    # retranslateUi

