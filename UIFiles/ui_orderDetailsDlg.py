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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_OrderDetailsDlg(object):
    def setupUi(self, OrderDetailsDlg):
        if not OrderDetailsDlg.objectName():
            OrderDetailsDlg.setObjectName(u"OrderDetailsDlg")
        OrderDetailsDlg.resize(580, 526)
        self.formLayout_4 = QFormLayout(OrderDetailsDlg)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lblOrderDetails = QLabel(OrderDetailsDlg)
        self.lblOrderDetails.setObjectName(u"lblOrderDetails")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblOrderDetails.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.lblOrderDetails)

        self.line = QFrame(OrderDetailsDlg)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setBold(False)
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.line)

        self.frame = QFrame(OrderDetailsDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lblStkSymbol = QLabel(self.frame)
        self.lblStkSymbol.setObjectName(u"lblStkSymbol")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lblStkSymbol.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.lblStkSymbol)

        self.lblQuantityVal = QLabel(self.frame)
        self.lblQuantityVal.setObjectName(u"lblQuantityVal")
        self.lblQuantityVal.setFont(font2)

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.lblQuantityVal)


        self.formLayout_4.setWidget(2, QFormLayout.SpanningRole, self.frame)

        self.line_2 = QFrame(OrderDetailsDlg)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(100, 0))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout_4.setWidget(3, QFormLayout.SpanningRole, self.line_2)

        self.frame_2 = QFrame(OrderDetailsDlg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.lblOrderType = QLabel(self.frame_2)
        self.lblOrderType.setObjectName(u"lblOrderType")
        font3 = QFont()
        font3.setBold(True)
        self.lblOrderType.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblOrderType)

        self.lblOrderTypeVal = QLabel(self.frame_2)
        self.lblOrderTypeVal.setObjectName(u"lblOrderTypeVal")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lblOrderTypeVal)

        self.lblOrderPrice = QLabel(self.frame_2)
        self.lblOrderPrice.setObjectName(u"lblOrderPrice")
        self.lblOrderPrice.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblOrderPrice)

        self.lblOrderPriceVal = QLabel(self.frame_2)
        self.lblOrderPriceVal.setObjectName(u"lblOrderPriceVal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lblOrderPriceVal)

        self.lblAvgPrice = QLabel(self.frame_2)
        self.lblAvgPrice.setObjectName(u"lblAvgPrice")
        self.lblAvgPrice.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblAvgPrice)

        self.lblAvgPriceVal = QLabel(self.frame_2)
        self.lblAvgPriceVal.setObjectName(u"lblAvgPriceVal")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lblAvgPriceVal)

        self.lblExchange = QLabel(self.frame_2)
        self.lblExchange.setObjectName(u"lblExchange")
        self.lblExchange.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblExchange)

        self.lblExchangeVal = QLabel(self.frame_2)
        self.lblExchangeVal.setObjectName(u"lblExchangeVal")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lblExchangeVal)


        self.formLayout_4.setWidget(4, QFormLayout.SpanningRole, self.frame_2)

        self.line_3 = QFrame(OrderDetailsDlg)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(100, 0))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout_4.setWidget(5, QFormLayout.SpanningRole, self.line_3)

        self.frame_3 = QFrame(OrderDetailsDlg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblOrderStatus = QLabel(self.frame_3)
        self.lblOrderStatus.setObjectName(u"lblOrderStatus")
        self.lblOrderStatus.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblOrderStatus)

        self.lblOrderStatusVal = QLabel(self.frame_3)
        self.lblOrderStatusVal.setObjectName(u"lblOrderStatusVal")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lblOrderStatusVal)

        self.lblReqReceived = QLabel(self.frame_3)
        self.lblReqReceived.setObjectName(u"lblReqReceived")
        self.lblReqReceived.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblReqReceived)

        self.lblReqReceivedVal = QLabel(self.frame_3)
        self.lblReqReceivedVal.setObjectName(u"lblReqReceivedVal")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lblReqReceivedVal)

        self.lblOrderId = QLabel(self.frame_3)
        self.lblOrderId.setObjectName(u"lblOrderId")
        self.lblOrderId.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lblOrderId)

        self.lblOrderIdVal = QLabel(self.frame_3)
        self.lblOrderIdVal.setObjectName(u"lblOrderIdVal")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lblOrderIdVal)

        self.lblOrderPlaced = QLabel(self.frame_3)
        self.lblOrderPlaced.setObjectName(u"lblOrderPlaced")
        self.lblOrderPlaced.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lblOrderPlaced)

        self.lblOrderPlacedVal = QLabel(self.frame_3)
        self.lblOrderPlacedVal.setObjectName(u"lblOrderPlacedVal")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lblOrderPlacedVal)

        self.lblExchOrderId = QLabel(self.frame_3)
        self.lblExchOrderId.setObjectName(u"lblExchOrderId")
        self.lblExchOrderId.setFont(font3)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lblExchOrderId)

        self.lblExchOrderIdVal = QLabel(self.frame_3)
        self.lblExchOrderIdVal.setObjectName(u"lblExchOrderIdVal")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lblExchOrderIdVal)


        self.formLayout_4.setWidget(6, QFormLayout.SpanningRole, self.frame_3)

        self.frmButtons = QFrame(OrderDetailsDlg)
        self.frmButtons.setObjectName(u"frmButtons")
        self.frmButtons.setMinimumSize(QSize(100, 0))
        self.frmButtons.setFrameShape(QFrame.StyledPanel)
        self.frmButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frmButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.frmButtons)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnModify = QPushButton(self.frmButtons)
        self.btnModify.setObjectName(u"btnModify")

        self.horizontalLayout.addWidget(self.btnModify)


        self.formLayout_4.setWidget(7, QFormLayout.SpanningRole, self.frmButtons)


        self.retranslateUi(OrderDetailsDlg)

        QMetaObject.connectSlotsByName(OrderDetailsDlg)
    # setupUi

    def retranslateUi(self, OrderDetailsDlg):
        OrderDetailsDlg.setWindowTitle(QCoreApplication.translate("OrderDetailsDlg", u"Form", None))
        self.lblOrderDetails.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order Details", None))
        self.lblStkSymbol.setText(QCoreApplication.translate("OrderDetailsDlg", u"Symbol Name", None))
        self.lblQuantityVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"Quantity", None))
        self.lblOrderType.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order type", None))
        self.lblOrderTypeVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblOrderPrice.setText(QCoreApplication.translate("OrderDetailsDlg", u"Order price", None))
        self.lblOrderPriceVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblAvgPrice.setText(QCoreApplication.translate("OrderDetailsDlg", u"Avg price", None))
        self.lblAvgPriceVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
        self.lblExchange.setText(QCoreApplication.translate("OrderDetailsDlg", u"Exchange", None))
        self.lblExchangeVal.setText(QCoreApplication.translate("OrderDetailsDlg", u"TextLabel", None))
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
        self.btnCancel.setText(QCoreApplication.translate("OrderDetailsDlg", u"Cancel", None))
        self.btnModify.setText(QCoreApplication.translate("OrderDetailsDlg", u"Modify", None))
    # retranslateUi

