# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderDetailsDlg.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_OrderDetailsDlg(object):
    def setupUi(self, OrderDetailsDlg):
        if not OrderDetailsDlg.objectName():
            OrderDetailsDlg.setObjectName(u"OrderDetailsDlg")
        OrderDetailsDlg.resize(472, 602)
        self.gridLayout_2 = QGridLayout(OrderDetailsDlg)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lblOrderDetails = QLabel(OrderDetailsDlg)
        self.lblOrderDetails.setObjectName(u"lblOrderDetails")
        self.lblOrderDetails.setMinimumSize(QSize(0, 70))
        self.lblOrderDetails.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblOrderDetails.setFont(font)
        self.lblOrderDetails.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color: white;\n"
"}")
        self.lblOrderDetails.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblOrderDetails, 0, 0, 1, 1)

        self.frame_4 = QFrame(OrderDetailsDlg)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(50, 0))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius : 15px;\n"
"	background-color:  white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(100, 0))
        self.line_3.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 1)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(100, 0))
        self.line_2.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lblStkSymbol = QLabel(self.frame)
        self.lblStkSymbol.setObjectName(u"lblStkSymbol")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblStkSymbol.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.lblStkSymbol)

        self.lblQuantityVal = QLabel(self.frame)
        self.lblQuantityVal.setObjectName(u"lblQuantityVal")
        self.lblQuantityVal.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.lblQuantityVal)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblOrderStatus = QLabel(self.frame_3)
        self.lblOrderStatus.setObjectName(u"lblOrderStatus")
        font2 = QFont()
        font2.setBold(True)
        self.lblOrderStatus.setFont(font2)

        self.gridLayout_3.addWidget(self.lblOrderStatus, 0, 0, 1, 1)

        self.lblOrderStatusVal = QLabel(self.frame_3)
        self.lblOrderStatusVal.setObjectName(u"lblOrderStatusVal")

        self.gridLayout_3.addWidget(self.lblOrderStatusVal, 0, 1, 1, 1)

        self.lblReqReceived = QLabel(self.frame_3)
        self.lblReqReceived.setObjectName(u"lblReqReceived")
        self.lblReqReceived.setFont(font2)

        self.gridLayout_3.addWidget(self.lblReqReceived, 1, 0, 1, 1)

        self.lblReqReceivedVal = QLabel(self.frame_3)
        self.lblReqReceivedVal.setObjectName(u"lblReqReceivedVal")

        self.gridLayout_3.addWidget(self.lblReqReceivedVal, 1, 1, 1, 1)

        self.lblOrderId = QLabel(self.frame_3)
        self.lblOrderId.setObjectName(u"lblOrderId")
        self.lblOrderId.setFont(font2)

        self.gridLayout_3.addWidget(self.lblOrderId, 2, 0, 1, 1)

        self.lblOrderIdVal = QLabel(self.frame_3)
        self.lblOrderIdVal.setObjectName(u"lblOrderIdVal")

        self.gridLayout_3.addWidget(self.lblOrderIdVal, 2, 1, 1, 1)

        self.lblOrderPlaced = QLabel(self.frame_3)
        self.lblOrderPlaced.setObjectName(u"lblOrderPlaced")
        self.lblOrderPlaced.setFont(font2)

        self.gridLayout_3.addWidget(self.lblOrderPlaced, 3, 0, 1, 1)

        self.lblOrderPlacedVal = QLabel(self.frame_3)
        self.lblOrderPlacedVal.setObjectName(u"lblOrderPlacedVal")

        self.gridLayout_3.addWidget(self.lblOrderPlacedVal, 3, 1, 1, 1)

        self.lblExchOrderId = QLabel(self.frame_3)
        self.lblExchOrderId.setObjectName(u"lblExchOrderId")
        self.lblExchOrderId.setFont(font2)

        self.gridLayout_3.addWidget(self.lblExchOrderId, 4, 0, 1, 1)

        self.lblExchOrderIdVal = QLabel(self.frame_3)
        self.lblExchOrderIdVal.setObjectName(u"lblExchOrderIdVal")

        self.gridLayout_3.addWidget(self.lblExchOrderIdVal, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lblOrderType = QLabel(self.frame_2)
        self.lblOrderType.setObjectName(u"lblOrderType")
        self.lblOrderType.setFont(font2)

        self.gridLayout_4.addWidget(self.lblOrderType, 0, 0, 1, 1)

        self.lblOrderTypeVal = QLabel(self.frame_2)
        self.lblOrderTypeVal.setObjectName(u"lblOrderTypeVal")

        self.gridLayout_4.addWidget(self.lblOrderTypeVal, 0, 1, 1, 1)

        self.lblOrderPrice = QLabel(self.frame_2)
        self.lblOrderPrice.setObjectName(u"lblOrderPrice")
        self.lblOrderPrice.setFont(font2)

        self.gridLayout_4.addWidget(self.lblOrderPrice, 1, 0, 1, 1)

        self.lblOrderPriceVal = QLabel(self.frame_2)
        self.lblOrderPriceVal.setObjectName(u"lblOrderPriceVal")

        self.gridLayout_4.addWidget(self.lblOrderPriceVal, 1, 1, 1, 1)

        self.lblAvgPrice = QLabel(self.frame_2)
        self.lblAvgPrice.setObjectName(u"lblAvgPrice")
        self.lblAvgPrice.setFont(font2)

        self.gridLayout_4.addWidget(self.lblAvgPrice, 2, 0, 1, 1)

        self.lblAvgPriceVal = QLabel(self.frame_2)
        self.lblAvgPriceVal.setObjectName(u"lblAvgPriceVal")

        self.gridLayout_4.addWidget(self.lblAvgPriceVal, 2, 1, 1, 1)

        self.lblExchange = QLabel(self.frame_2)
        self.lblExchange.setObjectName(u"lblExchange")
        self.lblExchange.setFont(font2)

        self.gridLayout_4.addWidget(self.lblExchange, 3, 0, 1, 1)

        self.lblExchangeVal = QLabel(self.frame_2)
        self.lblExchangeVal.setObjectName(u"lblExchangeVal")

        self.gridLayout_4.addWidget(self.lblExchangeVal, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.frmButtons = QFrame(self.frame_4)
        self.frmButtons.setObjectName(u"frmButtons")
        self.frmButtons.setMinimumSize(QSize(100, 0))
        self.frmButtons.setMaximumSize(QSize(16777215, 100))
        self.frmButtons.setFrameShape(QFrame.StyledPanel)
        self.frmButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frmButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.frmButtons)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 45))
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

        self.btnModify = QPushButton(self.frmButtons)
        self.btnModify.setObjectName(u"btnModify")
        self.btnModify.setMinimumSize(QSize(0, 45))
        self.btnModify.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btnModify)


        self.gridLayout.addWidget(self.frmButtons, 6, 0, 1, 1)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid black;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)


        self.retranslateUi(OrderDetailsDlg)

        QMetaObject.connectSlotsByName(OrderDetailsDlg)
    # setupUi

    def retranslateUi(self, OrderDetailsDlg):
        OrderDetailsDlg.setWindowTitle(QCoreApplication.translate("OrderDetailsDlg", u"Form", None))
        self.lblOrderDetails.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order Details", None))
        self.lblStkSymbol.setText(QCoreApplication.translate("OrderDetailsDlg", u"Symbol Name", None))
        self.lblQuantityVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"Quantity", None))
        self.lblOrderStatus.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order status", None))
        self.lblOrderStatusVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblReqReceived.setText(QCoreApplication.translate("OrderDetailsDlg", u"Request received", None))
        self.lblReqReceivedVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblOrderId.setText(QCoreApplication.translate("OrderDetailsDlg", u"order id", None))
        self.lblOrderIdVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblOrderPlaced.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order Placed", None))
        self.lblOrderPlacedVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblExchOrderId.setText(QCoreApplication.translate("OrderDetailsDlg", u"exchange order id", None))
        self.lblExchOrderIdVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblOrderType.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order type", None))
        self.lblOrderTypeVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblOrderPrice.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order price", None))
        self.lblOrderPriceVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblAvgPrice.setText(QCoreApplication.translate("OrderDetailsDlg", u"Avg price", None))
        self.lblAvgPriceVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblExchange.setText(QCoreApplication.translate("OrderDetailsDlg", u"Exchange", None))
        self.lblExchangeVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.btnCancel.setText(QCoreApplication.translate("OrderDetailsDlg", u"Cancel", None))
        self.btnModify.setText(QCoreApplication.translate("OrderDetailsDlg", u"Modify", None))
    # retranslateUi

