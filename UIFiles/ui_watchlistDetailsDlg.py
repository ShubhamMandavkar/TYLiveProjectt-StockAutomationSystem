# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watchlistDetailsDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_watchlistDetails(object):
    def setupUi(self, watchlistDetails):
        if not watchlistDetails.objectName():
            watchlistDetails.setObjectName(u"watchlistDetails")
        watchlistDetails.resize(462, 167)
        self.verticalLayout = QVBoxLayout(watchlistDetails)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(watchlistDetails)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblName = QLabel(self.frame_2)
        self.lblName.setObjectName(u"lblName")
        font = QFont()
        font.setPointSize(10)
        self.lblName.setFont(font)

        self.horizontalLayout.addWidget(self.lblName)

        self.leName = QLineEdit(self.frame_2)
        self.leName.setObjectName(u"leName")
        self.leName.setMinimumSize(QSize(0, 30))
        self.leName.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(239, 239, 239);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.leName)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 30))
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
"	background-color: #33b864;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50c878;\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnCreate = QPushButton(self.frame)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setMinimumSize(QSize(0, 30))
        self.btnCreate.setStyleSheet(u"QPushButton{\n"
"	background-color: #33b864;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50c878;\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnCreate)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(watchlistDetails)

        QMetaObject.connectSlotsByName(watchlistDetails)
    # setupUi

    def retranslateUi(self, watchlistDetails):
        watchlistDetails.setWindowTitle(QCoreApplication.translate("watchlistDetails", u"Dialog", None))
        self.lblName.setText(QCoreApplication.translate("watchlistDetails", u"Name : ", None))
        self.btnCancel.setText(QCoreApplication.translate("watchlistDetails", u"Cancel", None))
        self.btnCreate.setText(QCoreApplication.translate("watchlistDetails", u"Create", None))
    # retranslateUi

