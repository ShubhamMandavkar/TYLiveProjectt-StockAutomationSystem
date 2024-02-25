from PySide6.QtWidgets import QDialog
from ProjectPages.messageDlg import MessageDlg
from UIFiles.ui_orderDetailsDlg import Ui_OrderDetailsDlg
from ProjectPages.buyOrderDlg import BuyOrderDlg
from ProjectPages.sellOrderDlg import MyException, SellOrderDlg

class OrderDetailsDlg(QDialog):
    def __init__(self, userName, order, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDetailsDlg()
        self.ui.setupUi(self)
        self.setWindowTitle('Order')
        self.order = order
        self.userName = userName

        self.setDetails()
        if(self.order['status'] != 'open' and self.order['status'] != 'pending'):
            self.hideButtonsFrame()

        self.addConnectors()

    def addConnectors(self):
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnModify.clicked.connect(self.modifyOrder)
        self.ui.btnModify.clicked.connect(self.close)

    def setDetails(self):
        self.ui.lblStkSymbol.setText(self.order['symbol'])
        self.ui.lblQuantityVal.setText(str(int(self.order['quantity'])) + ' shares')
        self.ui.lblOrderTypeVal.setText(self.order['action'] + ', '+ self.order['product'])
        if(self.order['pricetype'] == 'MARKET'):
            self.ui.lblOrderPriceVal.setText(self.order['pricetype'] + 'price')
        else:
            self.ui.lblOrderPriceVal.setText(str(self.order['price']))

        self.ui.lblAvgPriceVal.setText(str(self.order['avgprc']))
        self.ui.lblExchangeVal.setText(self.order['exchange'])

        if(self.order['status'] == 'completed'):
            self.ui.lblOrderStatusVal.setText('successful')
        elif(self.order['status'] == 'rejected'):
            self.ui.lblOrderStatusVal.setText('failed')
        else:
            self.ui.lblOrderStatusVal.setText(self.order['status'])

        self.ui.lblReqReceivedVal.setText(self.order['orderentrytime'])
        self.ui.lblOrderIdVal.setText(self.order['order_id'])
        self.ui.lblOrderPlacedVal.setText(self.order['exchconfrmtime'])
        self.ui.lblExchOrderIdVal.setText(self.order['exchordid'])

    def modifyOrder(self):
        symbol , _ = self.order['symbol'].split('-')
        if(self.order['action'] == 'BUY'):
            self.orderDlg = BuyOrderDlg(symbol)
            self.orderDlg.setOrderDetails(self.order)
            self.orderDlg.ui.btnOrder.clicked.disconnect(self.orderDlg.placeBuyOrder)
            self.orderDlg.ui.btnOrder.clicked.connect(lambda:self.orderDlg.modifyOrder(self.order))
            self.orderDlg.show()
            print('Modified buy order')
        else:
            try:
                self.orderDlg = SellOrderDlg(self.userName, symbol)
                self.orderDlg.setOrderDetails(self.order)
                self.orderDlg.validateQuantity()
                self.orderDlg.ui.btnOrder.clicked.disconnect(self.orderDlg.placeSellOrder)
                self.orderDlg.ui.btnOrder.clicked.connect(lambda:self.orderDlg.modifyOrder(self.order))
                self.orderDlg.show()
                print('Modified sell order')
            except MyException as e:
                self.msgDlg = MessageDlg(e.msg)
                self.msgDlg.show()
                print(e)

    def hideButtonsFrame(self):
        self.ui.frmButtons.hide()