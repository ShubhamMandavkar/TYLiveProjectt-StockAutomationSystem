# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watchlists.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_watchlists(object):
    def setupUi(self, watchlists):
        if not watchlists.objectName():
            watchlists.setObjectName(u"watchlists")
        watchlists.resize(1005, 614)
        self.centralwidget = QWidget(watchlists)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cmbWatchlists = QComboBox(self.frame_3)
        self.cmbWatchlists.setObjectName(u"cmbWatchlists")

        self.verticalLayout_2.addWidget(self.cmbWatchlists)

        self.frmWLContent = QFrame(self.frame_3)
        self.frmWLContent.setObjectName(u"frmWLContent")
        self.frmWLContent.setFrameShape(QFrame.StyledPanel)
        self.frmWLContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmWLContent)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.frame_5 = QFrame(self.frmWLContent)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblMsg = QLabel(self.frame_5)
        self.lblMsg.setObjectName(u"lblMsg")
        self.lblMsg.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblMsg.setFont(font)
        self.lblMsg.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lblMsg)

        self.tbvWatchlist = QTableView(self.frame_5)
        self.tbvWatchlist.setObjectName(u"tbvWatchlist")
        self.tbvWatchlist.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbvWatchlist.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbvWatchlist.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tbvWatchlist)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frmWLOperations = QFrame(self.frmWLContent)
        self.frmWLOperations.setObjectName(u"frmWLOperations")
        self.frmWLOperations.setMinimumSize(QSize(100, 0))
        self.frmWLOperations.setFrameShape(QFrame.StyledPanel)
        self.frmWLOperations.setFrameShadow(QFrame.Raised)
        self.btnAddToWL = QPushButton(self.frmWLOperations)
        self.btnAddToWL.setObjectName(u"btnAddToWL")
        self.btnAddToWL.setGeometry(QRect(10, 10, 83, 29))
        self.btnDeleteFrmWL = QPushButton(self.frmWLOperations)
        self.btnDeleteFrmWL.setObjectName(u"btnDeleteFrmWL")
        self.btnDeleteFrmWL.setGeometry(QRect(10, 50, 83, 29))

        self.horizontalLayout_2.addWidget(self.frmWLOperations)


        self.verticalLayout_2.addWidget(self.frmWLContent)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.btnCreateWL = QPushButton(self.frame_7)
        self.btnCreateWL.setObjectName(u"btnCreateWL")
        self.btnCreateWL.setGeometry(QRect(30, 10, 83, 29))

        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_3)

        watchlists.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(watchlists)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1005, 25))
        watchlists.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(watchlists)
        self.statusbar.setObjectName(u"statusbar")
        watchlists.setStatusBar(self.statusbar)

        self.retranslateUi(watchlists)

        QMetaObject.connectSlotsByName(watchlists)
    # setupUi

    def retranslateUi(self, watchlists):
        watchlists.setWindowTitle(QCoreApplication.translate("watchlists", u"MainWindow", None))
        self.lblMsg.setText(QCoreApplication.translate("watchlists", u"No Stocks in Watchlist", None))
        self.btnAddToWL.setText(QCoreApplication.translate("watchlists", u"Add", None))
        self.btnDeleteFrmWL.setText(QCoreApplication.translate("watchlists", u"Delete", None))
        self.btnCreateWL.setText(QCoreApplication.translate("watchlists", u"Create", None))
    # retranslateUi

