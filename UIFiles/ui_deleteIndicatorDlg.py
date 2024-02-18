# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteIndicatorDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_dlgDeleteIndicator(object):
    def setupUi(self, dlgDeleteIndicator):
        if not dlgDeleteIndicator.objectName():
            dlgDeleteIndicator.setObjectName(u"dlgDeleteIndicator")
        dlgDeleteIndicator.resize(356, 178)
        self.verticalLayout = QVBoxLayout(dlgDeleteIndicator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(dlgDeleteIndicator)
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
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.lblIndicatorName = QLabel(self.frame_2)
        self.lblIndicatorName.setObjectName(u"lblIndicatorName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblIndicatorName)

        self.lblLen = QLabel(self.frame_2)
        self.lblLen.setObjectName(u"lblLen")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblLen)

        self.lblLenVal = QLabel(self.frame_2)
        self.lblLenVal.setObjectName(u"lblLenVal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lblLenVal)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 35))
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(0, 35))
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

        self.horizontalLayout.addWidget(self.btnDelete)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(dlgDeleteIndicator)

        QMetaObject.connectSlotsByName(dlgDeleteIndicator)
    # setupUi

    def retranslateUi(self, dlgDeleteIndicator):
        dlgDeleteIndicator.setWindowTitle(QCoreApplication.translate("dlgDeleteIndicator", u"Dialog", None))
        self.lblIndicatorName.setText(QCoreApplication.translate("dlgDeleteIndicator", u"IndicatorName", None))
        self.lblLen.setText(QCoreApplication.translate("dlgDeleteIndicator", u"Length : ", None))
        self.lblLenVal.setText(QCoreApplication.translate("dlgDeleteIndicator", u"?", None))
        self.btnCancel.setText(QCoreApplication.translate("dlgDeleteIndicator", u"Cancel", None))
        self.btnDelete.setText(QCoreApplication.translate("dlgDeleteIndicator", u"Delete", None))
    # retranslateUi

