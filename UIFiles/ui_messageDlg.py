# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messageDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_dlgMessage(object):
    def setupUi(self, dlgMessage):
        if not dlgMessage.objectName():
            dlgMessage.setObjectName(u"dlgMessage")
        dlgMessage.resize(477, 129)
        self.verticalLayout = QVBoxLayout(dlgMessage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblMsg = QLabel(dlgMessage)
        self.lblMsg.setObjectName(u"lblMsg")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lblMsg.setFont(font)
        self.lblMsg.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblMsg)

        self.btnOk = QPushButton(dlgMessage)
        self.btnOk.setObjectName(u"btnOk")

        self.verticalLayout.addWidget(self.btnOk)


        self.retranslateUi(dlgMessage)

        QMetaObject.connectSlotsByName(dlgMessage)
    # setupUi

    def retranslateUi(self, dlgMessage):
        dlgMessage.setWindowTitle(QCoreApplication.translate("dlgMessage", u"Dialog", None))
        self.lblMsg.setText("")
        self.btnOk.setText(QCoreApplication.translate("dlgMessage", u"OK", None))
    # retranslateUi

