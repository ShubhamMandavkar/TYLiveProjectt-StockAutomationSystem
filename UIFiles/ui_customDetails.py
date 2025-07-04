# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customDetails.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_customDetails(object):
    def setupUi(self, customDetails):
        if not customDetails.objectName():
            customDetails.setObjectName(u"customDetails")
        customDetails.resize(827, 641)
        customDetails.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.centralwidget = QWidget(customDetails)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblHeading = QLabel(self.centralwidget)
        self.lblHeading.setObjectName(u"lblHeading")
        self.lblHeading.setMinimumSize(QSize(0, 80))
        self.lblHeading.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lblHeading.setFont(font)
        self.lblHeading.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}")
        self.lblHeading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblHeading)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.leApiKey = QLineEdit(self.frame_5)
        self.leApiKey.setObjectName(u"leApiKey")
        self.leApiKey.setMinimumSize(QSize(0, 40))
        self.leApiKey.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.leApiKey.setFont(font1)
        self.leApiKey.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")

        self.gridLayout.addWidget(self.leApiKey, 0, 1, 1, 1)

        self.cbTelegramNoti = QCheckBox(self.frame_5)
        self.cbTelegramNoti.setObjectName(u"cbTelegramNoti")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbTelegramNoti.sizePolicy().hasHeightForWidth())
        self.cbTelegramNoti.setSizePolicy(sizePolicy)
        self.cbTelegramNoti.setMinimumSize(QSize(0, 40))
        self.cbTelegramNoti.setMaximumSize(QSize(16777215, 40))
        self.cbTelegramNoti.setLayoutDirection(Qt.RightToLeft)
        self.cbTelegramNoti.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")

        self.gridLayout.addWidget(self.cbTelegramNoti, 7, 0, 1, 1)

        self.lblApiSecretKey = QLabel(self.frame_5)
        self.lblApiSecretKey.setObjectName(u"lblApiSecretKey")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.lblApiSecretKey.setFont(font2)
        self.lblApiSecretKey.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblApiSecretKey, 1, 0, 1, 1)

        self.lblTelegramNoti = QLabel(self.frame_5)
        self.lblTelegramNoti.setObjectName(u"lblTelegramNoti")
        self.lblTelegramNoti.setFont(font2)
        self.lblTelegramNoti.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblTelegramNoti, 7, 1, 1, 1)

        self.lblDesktopNoti = QLabel(self.frame_5)
        self.lblDesktopNoti.setObjectName(u"lblDesktopNoti")
        self.lblDesktopNoti.setFont(font2)
        self.lblDesktopNoti.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblDesktopNoti, 5, 1, 1, 1)

        self.cbDesktopNoti = QCheckBox(self.frame_5)
        self.cbDesktopNoti.setObjectName(u"cbDesktopNoti")
        sizePolicy.setHeightForWidth(self.cbDesktopNoti.sizePolicy().hasHeightForWidth())
        self.cbDesktopNoti.setSizePolicy(sizePolicy)
        self.cbDesktopNoti.setMinimumSize(QSize(0, 40))
        self.cbDesktopNoti.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(9)
        self.cbDesktopNoti.setFont(font3)
        self.cbDesktopNoti.setLayoutDirection(Qt.RightToLeft)
        self.cbDesktopNoti.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}")
        self.cbDesktopNoti.setIconSize(QSize(20, 20))
        self.cbDesktopNoti.setTristate(False)

        self.gridLayout.addWidget(self.cbDesktopNoti, 5, 0, 1, 1)

        self.leApiSecretKey = QLineEdit(self.frame_5)
        self.leApiSecretKey.setObjectName(u"leApiSecretKey")
        sizePolicy.setHeightForWidth(self.leApiSecretKey.sizePolicy().hasHeightForWidth())
        self.leApiSecretKey.setSizePolicy(sizePolicy)
        self.leApiSecretKey.setMinimumSize(QSize(0, 40))
        self.leApiSecretKey.setMaximumSize(QSize(16777215, 40))
        self.leApiSecretKey.setFont(font1)
        self.leApiSecretKey.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")

        self.gridLayout.addWidget(self.leApiSecretKey, 1, 1, 1, 1)

        self.lbProfitThrld = QLabel(self.frame_5)
        self.lbProfitThrld.setObjectName(u"lbProfitThrld")
        self.lbProfitThrld.setFont(font2)
        self.lbProfitThrld.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbProfitThrld, 2, 0, 1, 1)

        self.lblApiKey = QLabel(self.frame_5)
        self.lblApiKey.setObjectName(u"lblApiKey")
        self.lblApiKey.setFont(font2)
        self.lblApiKey.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblApiKey, 0, 0, 1, 1)

        self.lblAverageThrld = QLabel(self.frame_5)
        self.lblAverageThrld.setObjectName(u"lblAverageThrld")
        self.lblAverageThrld.setFont(font2)

        self.gridLayout.addWidget(self.lblAverageThrld, 3, 0, 1, 1)

        self.dsbProfitThrld = QDoubleSpinBox(self.frame_5)
        self.dsbProfitThrld.setObjectName(u"dsbProfitThrld")
        sizePolicy.setHeightForWidth(self.dsbProfitThrld.sizePolicy().hasHeightForWidth())
        self.dsbProfitThrld.setSizePolicy(sizePolicy)
        self.dsbProfitThrld.setMinimumSize(QSize(0, 40))
        self.dsbProfitThrld.setMaximumSize(QSize(16777215, 40))
        self.dsbProfitThrld.setFont(font1)
        self.dsbProfitThrld.setStyleSheet(u"QDoubleSpinBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")

        self.gridLayout.addWidget(self.dsbProfitThrld, 2, 1, 1, 1)

        self.dsbAverageThrld = QDoubleSpinBox(self.frame_5)
        self.dsbAverageThrld.setObjectName(u"dsbAverageThrld")
        sizePolicy.setHeightForWidth(self.dsbAverageThrld.sizePolicy().hasHeightForWidth())
        self.dsbAverageThrld.setSizePolicy(sizePolicy)
        self.dsbAverageThrld.setMinimumSize(QSize(0, 40))
        self.dsbAverageThrld.setMaximumSize(QSize(16777215, 40))
        self.dsbAverageThrld.setFont(font1)
        self.dsbAverageThrld.setStyleSheet(u"QDoubleSpinBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")

        self.gridLayout.addWidget(self.dsbAverageThrld, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame{\n"
"	border-bottom : 2px solid black;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.btnSave = QPushButton(self.frame_4)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(0, 45))
        self.btnSave.setMaximumSize(QSize(125, 50))
        self.btnSave.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addWidget(self.frame_4)

        customDetails.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(customDetails)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 25))
        customDetails.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(customDetails)
        self.statusbar.setObjectName(u"statusbar")
        customDetails.setStatusBar(self.statusbar)

        self.retranslateUi(customDetails)

        QMetaObject.connectSlotsByName(customDetails)
    # setupUi

    def retranslateUi(self, customDetails):
        customDetails.setWindowTitle(QCoreApplication.translate("customDetails", u"MainWindow", None))
        self.lblHeading.setText(QCoreApplication.translate("customDetails", u"Custom Details", None))
        self.cbTelegramNoti.setText("")
        self.lblApiSecretKey.setText(QCoreApplication.translate("customDetails", u"API Secret Key : ", None))
        self.lblTelegramNoti.setText(QCoreApplication.translate("customDetails", u"Telegram Notification ", None))
        self.lblDesktopNoti.setText(QCoreApplication.translate("customDetails", u"Desktop Notification ", None))
        self.cbDesktopNoti.setText("")
        self.lbProfitThrld.setText(QCoreApplication.translate("customDetails", u"Profit Threshold : ", None))
        self.lblApiKey.setText(QCoreApplication.translate("customDetails", u"API Key : ", None))
        self.lblAverageThrld.setText(QCoreApplication.translate("customDetails", u"Average Threshold :", None))
        self.btnSave.setText(QCoreApplication.translate("customDetails", u"Save", None))
    # retranslateUi

