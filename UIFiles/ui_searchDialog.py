# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_dlgSearch(object):
    def setupUi(self, dlgSearch):
        if not dlgSearch.objectName():
            dlgSearch.setObjectName(u"dlgSearch")
        dlgSearch.resize(869, 494)
        self.verticalLayout = QVBoxLayout(dlgSearch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(dlgSearch)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leSearch = QLineEdit(self.frame)
        self.leSearch.setObjectName(u"leSearch")
        self.leSearch.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.leSearch)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(dlgSearch)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(dlgSearch)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tblvSuggestions = QTableView(self.frame_3)
        self.tblvSuggestions.setObjectName(u"tblvSuggestions")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblvSuggestions.sizePolicy().hasHeightForWidth())
        self.tblvSuggestions.setSizePolicy(sizePolicy)
        self.tblvSuggestions.setMinimumSize(QSize(500, 300))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tblvSuggestions.setFont(font)
        self.tblvSuggestions.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblvSuggestions.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblvSuggestions.horizontalHeader().setVisible(False)
        self.tblvSuggestions.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.tblvSuggestions)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(dlgSearch)

        QMetaObject.connectSlotsByName(dlgSearch)
    # setupUi

    def retranslateUi(self, dlgSearch):
        dlgSearch.setWindowTitle(QCoreApplication.translate("dlgSearch", u"Dialog", None))
        self.leSearch.setInputMask("")
        self.leSearch.setText("")
        self.leSearch.setPlaceholderText(QCoreApplication.translate("dlgSearch", u"Search", None))
    # retranslateUi

