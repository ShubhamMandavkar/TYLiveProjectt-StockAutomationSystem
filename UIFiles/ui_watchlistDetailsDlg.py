# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watchlistDetailsDlg.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_watchlistDetails(object):
    def setupUi(self, watchlistDetails):
        if not watchlistDetails.objectName():
            watchlistDetails.setObjectName(u"watchlistDetails")
        watchlistDetails.resize(462, 167)
        self.verticalLayout = QVBoxLayout(watchlistDetails)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(watchlistDetails)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblName = QLabel(self.frame_2)
        self.lblName.setObjectName(u"lblName")

        self.horizontalLayout.addWidget(self.lblName)

        self.leName = QLineEdit(self.frame_2)
        self.leName.setObjectName(u"leName")

        self.horizontalLayout.addWidget(self.leName)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(watchlistDetails)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnCreate = QPushButton(self.frame)
        self.btnCreate.setObjectName(u"btnCreate")

        self.horizontalLayout_2.addWidget(self.btnCreate)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(watchlistDetails)

        QMetaObject.connectSlotsByName(watchlistDetails)
    # setupUi

    def retranslateUi(self, watchlistDetails):
        watchlistDetails.setWindowTitle(QCoreApplication.translate("watchlistDetails", u"Dialog", None))
        self.lblName.setText(QCoreApplication.translate("watchlistDetails", u"Name : ", None))
        self.btnCancel.setText(QCoreApplication.translate("watchlistDetails", u"Cancel", None))
        self.btnCreate.setText(QCoreApplication.translate("watchlistDetails", u"Create", None))
    # retranslateUi

