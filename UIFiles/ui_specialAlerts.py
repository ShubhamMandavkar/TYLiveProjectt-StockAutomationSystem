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
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_specialAlerts(object):
    def setupUi(self, specialAlerts):
        if not specialAlerts.objectName():
            specialAlerts.setObjectName(u"specialAlerts")
        specialAlerts.resize(826, 570)
        self.centralwidget = QWidget(specialAlerts)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblHeading = QLabel(self.centralwidget)
        self.lblHeading.setObjectName(u"lblHeading")
        self.lblHeading.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblHeading.setFont(font)

        self.verticalLayout.addWidget(self.lblHeading)

        self.tbvSpecialAlertsStkList = QTableView(self.centralwidget)
        self.tbvSpecialAlertsStkList.setObjectName(u"tbvSpecialAlertsStkList")
        self.tbvSpecialAlertsStkList.setMaximumSize(QSize(16777215, 400))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.tbvSpecialAlertsStkList.setFont(font1)
        self.tbvSpecialAlertsStkList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbvSpecialAlertsStkList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbvSpecialAlertsStkList.horizontalHeader().setVisible(True)
        self.tbvSpecialAlertsStkList.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tbvSpecialAlertsStkList)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnImport = QPushButton(self.frame)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setMinimumSize(QSize(0, 40))
        self.btnImport.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btnImport, 0, 1, 1, 1)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(0, 40))
        self.btnDelete.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btnDelete, 0, 2, 1, 1)

        self.btnAdd = QPushButton(self.frame)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(0, 40))
        self.btnAdd.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btnAdd, 0, 0, 1, 1)

        self.btnClearAll = QPushButton(self.frame)
        self.btnClearAll.setObjectName(u"btnClearAll")
        self.btnClearAll.setMinimumSize(QSize(0, 40))
        self.btnClearAll.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btnClearAll, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        specialAlerts.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(specialAlerts)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 826, 25))
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
        self.btnImport.setText(QCoreApplication.translate("specialAlerts", u"Import", None))
        self.btnDelete.setText(QCoreApplication.translate("specialAlerts", u"Delete", None))
        self.btnAdd.setText(QCoreApplication.translate("specialAlerts", u"Add", None))
        self.btnClearAll.setText(QCoreApplication.translate("specialAlerts", u"ClearAll", None))
    # retranslateUi

