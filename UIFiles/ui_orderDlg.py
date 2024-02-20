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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_OrderDlg(object):
    def setupUi(self, OrderDlg):
        if not OrderDlg.objectName():
            OrderDlg.setObjectName(u"OrderDlg")
        OrderDlg.resize(415, 241)
        self.gridLayout_2 = QGridLayout(OrderDlg)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(7)
        self.lblStkSymbol = QLabel(OrderDlg)
        self.lblStkSymbol.setObjectName(u"lblStkSymbol")
        self.lblStkSymbol.setMinimumSize(QSize(0, 30))
        self.lblStkSymbol.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblStkSymbol.setFont(font)
        self.lblStkSymbol.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}")
        self.lblStkSymbol.setAlignment(Qt.AlignCenter)
        self.lblStkSymbol.setMargin(0)

        self.gridLayout_2.addWidget(self.lblStkSymbol, 0, 0, 1, 1)

        self.frame_2 = QFrame(OrderDlg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 130))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lblQuantity = QLabel(self.frame)
        self.lblQuantity.setObjectName(u"lblQuantity")
        font1 = QFont()
        font1.setPointSize(10)
        self.lblQuantity.setFont(font1)
        self.lblQuantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lblQuantity, 0, 0, 1, 1)

        self.sbQuantity = QSpinBox(self.frame)
        self.sbQuantity.setObjectName(u"sbQuantity")
        self.sbQuantity.setMinimumSize(QSize(0, 30))
        self.sbQuantity.setFont(font1)
        self.sbQuantity.setStyleSheet(u"QSpinBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")
        self.sbQuantity.setMaximum(1000000000)

        self.gridLayout_3.addWidget(self.sbQuantity, 0, 1, 1, 1)

        self.lblAvailQuantity = QLabel(self.frame)
        self.lblAvailQuantity.setObjectName(u"lblAvailQuantity")
        self.lblAvailQuantity.setFont(font1)
        self.lblAvailQuantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lblAvailQuantity, 1, 0, 1, 1)

        self.lblAvailQuantityVal = QLabel(self.frame)
        self.lblAvailQuantityVal.setObjectName(u"lblAvailQuantityVal")
        self.lblAvailQuantityVal.setFont(font1)

        self.gridLayout_3.addWidget(self.lblAvailQuantityVal, 1, 1, 1, 1)

        self.cmbPriceType = QComboBox(self.frame)
        self.cmbPriceType.addItem("")
        self.cmbPriceType.addItem("")
        self.cmbPriceType.addItem("")
        self.cmbPriceType.addItem("")
        self.cmbPriceType.setObjectName(u"cmbPriceType")
        self.cmbPriceType.setMinimumSize(QSize(100, 30))
        self.cmbPriceType.setFont(font1)
        self.cmbPriceType.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")

        self.gridLayout_3.addWidget(self.cmbPriceType, 2, 0, 1, 1)

        self.dsbPriceValue = QDoubleSpinBox(self.frame)
        self.dsbPriceValue.setObjectName(u"dsbPriceValue")
        self.dsbPriceValue.setMinimumSize(QSize(0, 30))
        self.dsbPriceValue.setFont(font1)
        self.dsbPriceValue.setStyleSheet(u"QDoubleSpinBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	border-radius : 5px;\n"
"}")
        self.dsbPriceValue.setMaximum(1000000000.000000000000000)

        self.gridLayout_3.addWidget(self.dsbPriceValue, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.btnOrder = QPushButton(self.frame_2)
        self.btnOrder.setObjectName(u"btnOrder")
        self.btnOrder.setMinimumSize(QSize(0, 45))
        self.btnOrder.setMaximumSize(QSize(16777215, 45))
        self.btnOrder.setStyleSheet(u"QPushButton{\n"
"	background-color: #2AAA8A;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"	padding: 5px;	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(46, 186, 151);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border : 1px solid black;\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout.addWidget(self.btnOrder, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)


        self.retranslateUi(OrderDlg)

        QMetaObject.connectSlotsByName(OrderDlg)
    # setupUi

    def retranslateUi(self, OrderDlg):
        OrderDlg.setWindowTitle(QCoreApplication.translate("OrderDlg", u"Form", None))
        self.lblStkSymbol.setText(QCoreApplication.translate("OrderDlg", u"Symbol Name", None))
        self.lblQuantity.setText(QCoreApplication.translate("OrderDlg", u"Quantity : ", None))
        self.lblAvailQuantity.setText(QCoreApplication.translate("OrderDlg", u"Available Quantity : ", None))
        self.lblAvailQuantityVal.setText(QCoreApplication.translate("OrderDlg", u"0", None))
        self.cmbPriceType.setItemText(0, QCoreApplication.translate("OrderDlg", u"MARKET", None))
        self.cmbPriceType.setItemText(1, QCoreApplication.translate("OrderDlg", u"LIMIT", None))
        self.cmbPriceType.setItemText(2, QCoreApplication.translate("OrderDlg", u"SL", None))
        self.cmbPriceType.setItemText(3, QCoreApplication.translate("OrderDlg", u"SL-M", None))

        self.btnOrder.setText(QCoreApplication.translate("OrderDlg", u"OK", None))
    # retranslateUi

