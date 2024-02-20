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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_myAlerts(object):
    def setupUi(self, myAlerts):
        if not myAlerts.objectName():
            myAlerts.setObjectName(u"myAlerts")
        myAlerts.resize(896, 548)
        myAlerts.setStyleSheet(u"background-color: rgb(239, 239, 239);")
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
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lsvMyAlerts = QListView(self.frame_3)
        self.lsvMyAlerts.setObjectName(u"lsvMyAlerts")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lsvMyAlerts.setFont(font1)
        self.lsvMyAlerts.setStyleSheet(u"QListView{\n"
"	border : 2px solid black;\n"
"	border-radius : 5px;\n"
"}")
        self.lsvMyAlerts.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.lsvMyAlerts.setAlternatingRowColors(True)
        self.lsvMyAlerts.setProperty("isWrapping", False)
        self.lsvMyAlerts.setResizeMode(QListView.Adjust)
        self.lsvMyAlerts.setSpacing(2)
        self.lsvMyAlerts.setWordWrap(True)

        self.verticalLayout.addWidget(self.lsvMyAlerts)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnPause = QPushButton(self.frame)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setMinimumSize(QSize(0, 45))
        self.btnPause.setMaximumSize(QSize(125, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.btnPause.setFont(font2)
        self.btnPause.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btnPause)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(0, 45))
        self.btnDelete.setMaximumSize(QSize(125, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.btnDelete.setFont(font3)
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

        self.horizontalLayout_3.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_4)

        myAlerts.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(myAlerts)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 896, 25))
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
        self.btnPause.setText(QCoreApplication.translate("myAlerts", u"Pause", None))
        self.btnDelete.setText(QCoreApplication.translate("myAlerts", u"Delete", None))
    # retranslateUi

