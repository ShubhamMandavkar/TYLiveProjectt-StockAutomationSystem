# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'holdings.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_holdings(object):
    def setupUi(self, holdings):
        if not holdings.objectName():
            holdings.setObjectName(u"holdings")
        holdings.resize(990, 558)
        self.centralwidget = QWidget(holdings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_4)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.lblHeading = QLabel(self.frame_4)
        self.lblHeading.setObjectName(u"lblHeading")
        self.lblHeading.setMinimumSize(QSize(0, 50))
        self.lblHeading.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setKerning(False)
        self.lblHeading.setFont(font)
        self.lblHeading.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.lblHeading)

        self.lblNoHoldingsMsg = QLabel(self.frame_4)
        self.lblNoHoldingsMsg.setObjectName(u"lblNoHoldingsMsg")
        self.lblNoHoldingsMsg.setMinimumSize(QSize(0, 50))
        self.lblNoHoldingsMsg.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblNoHoldingsMsg.setFont(font1)
        self.lblNoHoldingsMsg.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblNoHoldingsMsg.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.lblNoHoldingsMsg)

        self.tvHoldings = QTableView(self.frame_4)
        self.tvHoldings.setObjectName(u"tvHoldings")
        self.tvHoldings.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.tvHoldings.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tvHoldings.setSortingEnabled(True)
        self.tvHoldings.verticalHeader().setVisible(False)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.tvHoldings)


        self.horizontalLayout.addWidget(self.frame_4)

        holdings.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(holdings)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 25))
        holdings.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(holdings)
        self.statusbar.setObjectName(u"statusbar")
        holdings.setStatusBar(self.statusbar)

        self.retranslateUi(holdings)

        QMetaObject.connectSlotsByName(holdings)
    # setupUi

    def retranslateUi(self, holdings):
        holdings.setWindowTitle(QCoreApplication.translate("holdings", u"MainWindow", None))
        self.lblHeading.setText(QCoreApplication.translate("holdings", u"Holdings", None))
        self.lblNoHoldingsMsg.setText(QCoreApplication.translate("holdings", u"Currently you do not have any holdings in your porfolio.", None))
    # retranslateUi

