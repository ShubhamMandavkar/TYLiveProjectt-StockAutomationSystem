from PySide6.QtWidgets import QDialog
from UIFiles.ui_orderDetailsDlg import Ui_OrderDetailsDlg


class OrderDetailsDlg(QDialog):
    def __init__(self, order, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDetailsDlg()
        self.ui.setupUi(self)
        self.order = order

        self.setDetails()
        if(self.order['status'] != 'open'):
            self.hideButtonsFrame()
    
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

    def hideButtonsFrame(self):
        self.ui.frmButtons.hide()