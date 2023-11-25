# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customDetails.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_customDetails(object):
    def setupUi(self, customDetails):
        if not customDetails.objectName():
            customDetails.setObjectName(u"customDetails")
        customDetails.resize(971, 586)
        self.centralwidget = QWidget(customDetails)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frmNavBar = QFrame(self.centralwidget)
        self.frmNavBar.setObjectName(u"frmNavBar")
        self.frmNavBar.setMinimumSize(QSize(250, 0))
        self.frmNavBar.setMaximumSize(QSize(250, 16777215))
        self.frmNavBar.setFrameShape(QFrame.StyledPanel)
        self.frmNavBar.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frmNavBar)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.btnMyAlerts = QPushButton(self.frmNavBar)
        self.btnMyAlerts.setObjectName(u"btnMyAlerts")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.btnMyAlerts)

        self.btnHoldings = QPushButton(self.frmNavBar)
        self.btnHoldings.setObjectName(u"btnHoldings")

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.btnHoldings)

        self.btnCustomDetails = QPushButton(self.frmNavBar)
        self.btnCustomDetails.setObjectName(u"btnCustomDetails")

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.btnCustomDetails)

        self.btnWatchlists = QPushButton(self.frmNavBar)
        self.btnWatchlists.setObjectName(u"btnWatchlists")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.btnWatchlists)

        self.btnHome = QPushButton(self.frmNavBar)
        self.btnHome.setObjectName(u"btnHome")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.btnHome)


        self.horizontalLayout.addWidget(self.frmNavBar)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
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
        self.lblHeading = QLabel(self.frame_4)
        self.lblHeading.setObjectName(u"lblHeading")
        self.lblHeading.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblHeading.setFont(font)

        self.verticalLayout_2.addWidget(self.lblHeading)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(500, 300))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_5)
        self.formLayout.setObjectName(u"formLayout")
        self.lblApiKey = QLabel(self.frame_5)
        self.lblApiKey.setObjectName(u"lblApiKey")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblApiKey)

        self.leApiKey = QLineEdit(self.frame_5)
        self.leApiKey.setObjectName(u"leApiKey")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leApiKey)

        self.lblApiSecretKey = QLabel(self.frame_5)
        self.lblApiSecretKey.setObjectName(u"lblApiSecretKey")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblApiSecretKey)

        self.lbProfitThrld = QLabel(self.frame_5)
        self.lbProfitThrld.setObjectName(u"lbProfitThrld")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbProfitThrld)

        self.lblAverageThrld = QLabel(self.frame_5)
        self.lblAverageThrld.setObjectName(u"lblAverageThrld")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblAverageThrld)

        self.lblQuantity = QLabel(self.frame_5)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lblQuantity)

        self.leApiSecretKey = QLineEdit(self.frame_5)
        self.leApiSecretKey.setObjectName(u"leApiSecretKey")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leApiSecretKey)

        self.dsbProfitThrld = QDoubleSpinBox(self.frame_5)
        self.dsbProfitThrld.setObjectName(u"dsbProfitThrld")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dsbProfitThrld)

        self.dsbAverageThrld = QDoubleSpinBox(self.frame_5)
        self.dsbAverageThrld.setObjectName(u"dsbAverageThrld")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dsbAverageThrld)

        self.sbQuantity = QSpinBox(self.frame_5)
        self.sbQuantity.setObjectName(u"sbQuantity")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sbQuantity)

        self.lblDesktopNoti = QLabel(self.frame_5)
        self.lblDesktopNoti.setObjectName(u"lblDesktopNoti")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lblDesktopNoti)

        self.lblWhatsappNoti = QLabel(self.frame_5)
        self.lblWhatsappNoti.setObjectName(u"lblWhatsappNoti")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lblWhatsappNoti)

        self.lblWhatsappNo = QLabel(self.frame_5)
        self.lblWhatsappNo.setObjectName(u"lblWhatsappNo")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lblWhatsappNo)

        self.leWhatsappNo = QLineEdit(self.frame_5)
        self.leWhatsappNo.setObjectName(u"leWhatsappNo")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.leWhatsappNo)

        self.cbDesktopNoti = QCheckBox(self.frame_5)
        self.cbDesktopNoti.setObjectName(u"cbDesktopNoti")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cbDesktopNoti)

        self.cbWhatsappNoti = QCheckBox(self.frame_5)
        self.cbWhatsappNoti.setObjectName(u"cbWhatsappNoti")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cbWhatsappNoti)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.btnSave = QPushButton(self.frame_4)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMaximumSize(QSize(100, 30))

        self.verticalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)

        customDetails.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(customDetails)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 25))
        customDetails.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(customDetails)
        self.statusbar.setObjectName(u"statusbar")
        customDetails.setStatusBar(self.statusbar)

        self.retranslateUi(customDetails)

        QMetaObject.connectSlotsByName(customDetails)
    # setupUi

    def retranslateUi(self, customDetails):
        customDetails.setWindowTitle(QCoreApplication.translate("customDetails", u"MainWindow", None))
        self.btnMyAlerts.setText(QCoreApplication.translate("customDetails", u"MyAlerts", None))
        self.btnHoldings.setText(QCoreApplication.translate("customDetails", u"Holdings", None))
        self.btnCustomDetails.setText(QCoreApplication.translate("customDetails", u"CustomDetails", None))
        self.btnWatchlists.setText(QCoreApplication.translate("customDetails", u"Watchlists", None))
        self.btnHome.setText(QCoreApplication.translate("customDetails", u"Home", None))
        self.lblHeading.setText(QCoreApplication.translate("customDetails", u"Custom Details", None))
        self.lblApiKey.setText(QCoreApplication.translate("customDetails", u"API Key : ", None))
        self.lblApiSecretKey.setText(QCoreApplication.translate("customDetails", u"API Secret Key : ", None))
        self.lbProfitThrld.setText(QCoreApplication.translate("customDetails", u"Profit Threshold : ", None))
        self.lblAverageThrld.setText(QCoreApplication.translate("customDetails", u"Average Threshold : ", None))
        self.lblQuantity.setText(QCoreApplication.translate("customDetails", u"Quantity : ", None))
        self.lblDesktopNoti.setText(QCoreApplication.translate("customDetails", u"Desktop Notification : ", None))
        self.lblWhatsappNoti.setText(QCoreApplication.translate("customDetails", u"Whatsapp Notification : ", None))
        self.lblWhatsappNo.setText(QCoreApplication.translate("customDetails", u"Whatsapp No : ", None))
        self.cbDesktopNoti.setText(QCoreApplication.translate("customDetails", u"CheckBox", None))
        self.cbWhatsappNoti.setText(QCoreApplication.translate("customDetails", u"CheckBox", None))
        self.btnSave.setText(QCoreApplication.translate("customDetails", u"Save", None))
    # retranslateUi

