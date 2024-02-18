# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specialAlerts.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_specialAlerts(object):
    def setupUi(self, specialAlerts):
        if not specialAlerts.objectName():
            specialAlerts.setObjectName(u"specialAlerts")
        specialAlerts.resize(1011, 585)
        self.centralwidget = QWidget(specialAlerts)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblHeading = QLabel(self.centralwidget)
        self.lblHeading.setObjectName(u"lblHeading")
        self.lblHeading.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lblHeading.setFont(font)
        self.lblHeading.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}")
        self.lblHeading.setTextFormat(Qt.AutoText)
        self.lblHeading.setAlignment(Qt.AlignCenter)
        self.lblHeading.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblHeading)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(650, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lblStocksList = QLabel(self.frame_3)
        self.lblStocksList.setObjectName(u"lblStocksList")
        self.lblStocksList.setMinimumSize(QSize(0, 52))
        self.lblStocksList.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lblStocksList.setFont(font1)

        self.verticalLayout_3.addWidget(self.lblStocksList)

        self.tbvSpecialAlertsStkList = QTableView(self.frame_3)
        self.tbvSpecialAlertsStkList.setObjectName(u"tbvSpecialAlertsStkList")
        self.tbvSpecialAlertsStkList.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.tbvSpecialAlertsStkList.setFont(font2)
        self.tbvSpecialAlertsStkList.setStyleSheet(u"QTableView{\n"
"	border-radius : 5px;\n"
"	border: 2px solid black;\n"
"}")
        self.tbvSpecialAlertsStkList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbvSpecialAlertsStkList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbvSpecialAlertsStkList.setGridStyle(Qt.DotLine)
        self.tbvSpecialAlertsStkList.horizontalHeader().setVisible(True)
        self.tbvSpecialAlertsStkList.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tbvSpecialAlertsStkList)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.lblTodaysTriggeredList = QLabel(self.frame_5)
        self.lblTodaysTriggeredList.setObjectName(u"lblTodaysTriggeredList")
        self.lblTodaysTriggeredList.setMinimumSize(QSize(0, 40))
        self.lblTodaysTriggeredList.setMaximumSize(QSize(16777215, 100))
        self.lblTodaysTriggeredList.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lblTodaysTriggeredList)

        self.btnDownload = QPushButton(self.frame_5)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setMinimumSize(QSize(80, 45))
        self.btnDownload.setMaximumSize(QSize(125, 100))
        self.btnDownload.setStyleSheet(u"QPushButton{\n"
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
        self.btnDownload.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btnDownload)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.tbvTodaysTriggered = QTableView(self.frame_4)
        self.tbvTodaysTriggered.setObjectName(u"tbvTodaysTriggered")
        font3 = QFont()
        font3.setBold(True)
        self.tbvTodaysTriggered.setFont(font3)
        self.tbvTodaysTriggered.setStyleSheet(u"QTableView{\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"}")
        self.tbvTodaysTriggered.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbvTodaysTriggered.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbvTodaysTriggered.setGridStyle(Qt.DotLine)
        self.tbvTodaysTriggered.horizontalHeader().setDefaultSectionSize(150)
        self.tbvTodaysTriggered.horizontalHeader().setStretchLastSection(True)
        self.tbvTodaysTriggered.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tbvTodaysTriggered)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.lblNotification = QLabel(self.frame_6)
        self.lblNotification.setObjectName(u"lblNotification")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.lblNotification.setFont(font4)
        self.lblNotification.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblNotification)

        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnAdd = QPushButton(self.frame)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(0, 45))
        self.btnAdd.setMaximumSize(QSize(200, 16777215))
        self.btnAdd.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.btnAdd, 0, 0, 1, 1)

        self.btnClearAll = QPushButton(self.frame)
        self.btnClearAll.setObjectName(u"btnClearAll")
        self.btnClearAll.setMinimumSize(QSize(0, 45))
        self.btnClearAll.setMaximumSize(QSize(200, 16777215))
        self.btnClearAll.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.btnClearAll, 0, 3, 1, 1)

        self.btnImport = QPushButton(self.frame)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setMinimumSize(QSize(0, 45))
        self.btnImport.setMaximumSize(QSize(200, 16777215))
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

        self.gridLayout.addWidget(self.btnImport, 0, 1, 1, 1)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(0, 45))
        self.btnDelete.setMaximumSize(QSize(200, 16777215))
        self.btnDelete.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.btnDelete, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_6)

        specialAlerts.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(specialAlerts)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 25))
        specialAlerts.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(specialAlerts)
        self.statusbar.setObjectName(u"statusbar")
        specialAlerts.setStatusBar(self.statusbar)

        self.retranslateUi(specialAlerts)

        QMetaObject.connectSlotsByName(specialAlerts)
    # setupUi

    def retranslateUi(self, specialAlerts):
        specialAlerts.setWindowTitle(QCoreApplication.translate("specialAlerts", u"MainWindow", None))
        self.lblHeading.setText(QCoreApplication.translate("specialAlerts", u"Special Alerts", None))
        self.lblStocksList.setText(QCoreApplication.translate("specialAlerts", u"Stocks list", None))
        self.lblTodaysTriggeredList.setText(QCoreApplication.translate("specialAlerts", u"Today's Triggered list", None))
        self.btnDownload.setText(QCoreApplication.translate("specialAlerts", u"Download", None))
        self.lblNotification.setText("")
        self.btnAdd.setText(QCoreApplication.translate("specialAlerts", u"Add", None))
        self.btnClearAll.setText(QCoreApplication.translate("specialAlerts", u"ClearAll", None))
        self.btnImport.setText(QCoreApplication.translate("specialAlerts", u"Import", None))
        self.btnDelete.setText(QCoreApplication.translate("specialAlerts", u"Delete", None))
    # retranslateUi

