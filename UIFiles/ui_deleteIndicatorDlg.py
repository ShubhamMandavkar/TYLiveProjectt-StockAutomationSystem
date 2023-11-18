# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteIndicatorDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_dlgDeleteIndicator(object):
    def setupUi(self, dlgDeleteIndicator):
        if not dlgDeleteIndicator.objectName():
            dlgDeleteIndicator.setObjectName(u"dlgDeleteIndicator")
        dlgDeleteIndicator.resize(399, 153)
        self.verticalLayout = QVBoxLayout(dlgDeleteIndicator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(dlgDeleteIndicator)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lblIndicatorName = QLabel(self.frame_2)
        self.lblIndicatorName.setObjectName(u"lblIndicatorName")
        self.lblIndicatorName.setGeometry(QRect(12, 12, 351, 20))
        self.lblLen = QLabel(self.frame_2)
        self.lblLen.setObjectName(u"lblLen")
        self.lblLen.setGeometry(QRect(12, 39, 63, 20))
        self.lblLenVal = QLabel(self.frame_2)
        self.lblLenVal.setObjectName(u"lblLenVal")
        self.lblLenVal.setGeometry(QRect(70, 40, 63, 20))

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(dlgDeleteIndicator)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnDelete = QPushButton(self.frame)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.frame)


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

