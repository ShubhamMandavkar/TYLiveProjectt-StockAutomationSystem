# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_OrderDlg(object):
    def setupUi(self, OrderDlg):
        if not OrderDlg.objectName():
            OrderDlg.setObjectName(u"OrderDlg")
        OrderDlg.resize(496, 190)
        self.verticalLayout = QVBoxLayout(OrderDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblStkSymbol = QLabel(OrderDlg)
        self.lblStkSymbol.setObjectName(u"lblStkSymbol")
        self.lblStkSymbol.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblStkSymbol.setFont(font)
        self.lblStkSymbol.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblStkSymbol)

        self.frame = QFrame(OrderDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lblQuantity = QLabel(self.frame)
        self.lblQuantity.setObjectName(u"lblQuantity")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblQuantity)

        self.cmbPriceType = QComboBox(self.frame)
        self.cmbPriceType.addItem("")
        self.cmbPriceType.addItem("")
        self.cmbPriceType.addItem("")
        self.cmbPriceType.addItem("")
        self.cmbPriceType.setObjectName(u"cmbPriceType")
        self.cmbPriceType.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cmbPriceType)

        self.sbQuantity = QSpinBox(self.frame)
        self.sbQuantity.setObjectName(u"sbQuantity")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sbQuantity)

        self.dsbPriceValue = QDoubleSpinBox(self.frame)
        self.dsbPriceValue.setObjectName(u"dsbPriceValue")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dsbPriceValue)


        self.verticalLayout.addWidget(self.frame)

        self.btnOrder = QPushButton(OrderDlg)
        self.btnOrder.setObjectName(u"btnOrder")

        self.verticalLayout.addWidget(self.btnOrder)


        self.retranslateUi(OrderDlg)

        QMetaObject.connectSlotsByName(OrderDlg)
    # setupUi

    def retranslateUi(self, OrderDlg):
        OrderDlg.setWindowTitle(QCoreApplication.translate("OrderDlg", u"Form", None))
        self.lblStkSymbol.setText(QCoreApplication.translate("OrderDlg", u"Symbol Name", None))
        self.lblQuantity.setText(QCoreApplication.translate("OrderDlg", u"Quantity : ", None))
        self.cmbPriceType.setItemText(0, QCoreApplication.translate("OrderDlg", u"MARKET", None))
        self.cmbPriceType.setItemText(1, QCoreApplication.translate("OrderDlg", u"LIMIT", None))
        self.cmbPriceType.setItemText(2, QCoreApplication.translate("OrderDlg", u"SL", None))
        self.cmbPriceType.setItemText(3, QCoreApplication.translate("OrderDlg", u"SL-M", None))

        self.btnOrder.setText(QCoreApplication.translate("OrderDlg", u"OK", None))
    # retranslateUi

