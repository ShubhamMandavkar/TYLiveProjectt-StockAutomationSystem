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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

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

        self.lblApiSecreteKey = QLabel(self.frame_5)
        self.lblApiSecreteKey.setObjectName(u"lblApiSecreteKey")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblApiSecreteKey)

        self.lbProfitThrld = QLabel(self.frame_5)
        self.lbProfitThrld.setObjectName(u"lbProfitThrld")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbProfitThrld)

        self.lblAverageThrld = QLabel(self.frame_5)
        self.lblAverageThrld.setObjectName(u"lblAverageThrld")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblAverageThrld)

        self.lblQuantity = QLabel(self.frame_5)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lblQuantity)

        self.leApiSecreteKey = QLineEdit(self.frame_5)
        self.leApiSecreteKey.setObjectName(u"leApiSecreteKey")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leApiSecreteKey)

        self.dsbProftitThrld = QDoubleSpinBox(self.frame_5)
        self.dsbProftitThrld.setObjectName(u"dsbProftitThrld")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dsbProftitThrld)

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

        self.rbDesktopNoti = QRadioButton(self.frame_5)
        self.rbDesktopNoti.setObjectName(u"rbDesktopNoti")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.rbDesktopNoti)

        self.rbWhatsappNoti = QRadioButton(self.frame_5)
        self.rbWhatsappNoti.setObjectName(u"rbWhatsappNoti")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.rbWhatsappNoti)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 30))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblHeading.setText(QCoreApplication.translate("MainWindow", u"Custom Details", None))
        self.lblApiKey.setText(QCoreApplication.translate("MainWindow", u"API Key : ", None))
        self.lblApiSecreteKey.setText(QCoreApplication.translate("MainWindow", u"API Secrete Key : ", None))
        self.lbProfitThrld.setText(QCoreApplication.translate("MainWindow", u"Profit Threshold : ", None))
        self.lblAverageThrld.setText(QCoreApplication.translate("MainWindow", u"Average Threshold : ", None))
        self.lblQuantity.setText(QCoreApplication.translate("MainWindow", u"Quantity : ", None))
        self.lblDesktopNoti.setText(QCoreApplication.translate("MainWindow", u"Desktop Notification : ", None))
        self.lblWhatsappNoti.setText(QCoreApplication.translate("MainWindow", u"Whatsapp Notification : ", None))
        self.lblWhatsappNo.setText(QCoreApplication.translate("MainWindow", u"Whatsapp No : ", None))
        self.rbDesktopNoti.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.rbWhatsappNoti.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

