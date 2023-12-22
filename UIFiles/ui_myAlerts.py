# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myAlerts.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_myAlerts(object):
    def setupUi(self, myAlerts):
        if not myAlerts.objectName():
            myAlerts.setObjectName(u"myAlerts")
        myAlerts.resize(1140, 605)
        self.centralwidget = QWidget(myAlerts)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.lsvMyAlerts = QListView(self.frame_4)
        self.lsvMyAlerts.setObjectName(u"lsvMyAlerts")
        self.lsvMyAlerts.setFont(font)
        self.lsvMyAlerts.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.lsvMyAlerts.setAlternatingRowColors(True)
        self.lsvMyAlerts.setProperty("isWrapping", True)
        self.lsvMyAlerts.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.lsvMyAlerts)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btnDelete)

        self.btnPause = QPushButton(self.frame)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btnPause)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_4)

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
        self.label.setText(QCoreApplication.translate("myAlerts", u"My Alerts", None))
        self.btnDelete.setText(QCoreApplication.translate("myAlerts", u"Delete", None))
        self.btnPause.setText(QCoreApplication.translate("myAlerts", u"Pause", None))
    # retranslateUi

