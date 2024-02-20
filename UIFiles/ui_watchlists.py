# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watchlists.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_watchlists(object):
    def setupUi(self, watchlists):
        if not watchlists.objectName():
            watchlists.setObjectName(u"watchlists")
        watchlists.resize(964, 616)
        watchlists.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.centralwidget = QWidget(watchlists)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 80))
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

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frmWLContent = QFrame(self.frame_3)
        self.frmWLContent.setObjectName(u"frmWLContent")
        self.frmWLContent.setStyleSheet(u"")
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
        self.formLayout_2 = QFormLayout(self.frame_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.cmbWatchlists = QComboBox(self.frame_5)
        self.cmbWatchlists.setObjectName(u"cmbWatchlists")
        self.cmbWatchlists.setMinimumSize(QSize(0, 40))

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.cmbWatchlists)

        self.lblMsg = QLabel(self.frame_5)
        self.lblMsg.setObjectName(u"lblMsg")
        self.lblMsg.setMinimumSize(QSize(0, 40))
        self.lblMsg.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblMsg.setFont(font1)
        self.lblMsg.setAlignment(Qt.AlignCenter)
        self.lblMsg.setWordWrap(True)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.lblMsg)

        self.tbvWatchlist = QTableView(self.frame_5)
        self.tbvWatchlist.setObjectName(u"tbvWatchlist")
        self.tbvWatchlist.setStyleSheet(u"QTableView{\n"
"	border-radius : 5px;\n"
"	border: 2px solid black;\n"
"}")
        self.tbvWatchlist.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbvWatchlist.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbvWatchlist.horizontalHeader().setMinimumSectionSize(50)
        self.tbvWatchlist.horizontalHeader().setDefaultSectionSize(150)
        self.tbvWatchlist.horizontalHeader().setStretchLastSection(True)
        self.tbvWatchlist.verticalHeader().setVisible(False)

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.tbvWatchlist)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.line_2 = QFrame(self.frmWLContent)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame{\n"
"	border-left: 1px solid black;\n"
"}")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.frmWLOperations = QFrame(self.frmWLContent)
        self.frmWLOperations.setObjectName(u"frmWLOperations")
        self.frmWLOperations.setMinimumSize(QSize(125, 0))
        self.frmWLOperations.setMaximumSize(QSize(150, 16777215))
        self.frmWLOperations.setFrameShape(QFrame.StyledPanel)
        self.frmWLOperations.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frmWLOperations)
        self.formLayout.setObjectName(u"formLayout")
        self.btnAddToWL = QPushButton(self.frmWLOperations)
        self.btnAddToWL.setObjectName(u"btnAddToWL")
        self.btnAddToWL.setMinimumSize(QSize(0, 40))
        self.btnAddToWL.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btnAddToWL)

        self.btnDeleteFrmWL = QPushButton(self.frmWLOperations)
        self.btnDeleteFrmWL.setObjectName(u"btnDeleteFrmWL")
        self.btnDeleteFrmWL.setMinimumSize(QSize(0, 40))
        self.btnDeleteFrmWL.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btnDeleteFrmWL)

        self.btnImport = QPushButton(self.frmWLOperations)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setMinimumSize(QSize(0, 40))
        self.btnImport.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btnImport)


        self.horizontalLayout_2.addWidget(self.frmWLOperations)


        self.verticalLayout_2.addWidget(self.frmWLContent)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCreateWL = QPushButton(self.frame_7)
        self.btnCreateWL.setObjectName(u"btnCreateWL")
        self.btnCreateWL.setMinimumSize(QSize(125, 45))
        self.btnCreateWL.setMaximumSize(QSize(150, 16777215))
        self.btnCreateWL.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.btnCreateWL)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)

        watchlists.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(watchlists)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 964, 25))
        watchlists.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(watchlists)
        self.statusbar.setObjectName(u"statusbar")
        watchlists.setStatusBar(self.statusbar)

        self.retranslateUi(watchlists)

        QMetaObject.connectSlotsByName(watchlists)
    # setupUi

    def retranslateUi(self, watchlists):
        watchlists.setWindowTitle(QCoreApplication.translate("watchlists", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("watchlists", u"Watchlists", None))
        self.lblMsg.setText(QCoreApplication.translate("watchlists", u"No Stocks in Watchlist", None))
        self.btnAddToWL.setText(QCoreApplication.translate("watchlists", u"Add", None))
        self.btnDeleteFrmWL.setText(QCoreApplication.translate("watchlists", u"Delete", None))
        self.btnImport.setText(QCoreApplication.translate("watchlists", u"import", None))
        self.btnCreateWL.setText(QCoreApplication.translate("watchlists", u"Create", None))
    # retranslateUi

