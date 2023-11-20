from PySide6.QtCore import  QThread, QAbstractTableModel, Qt
from PySide6.QtWidgets import QMainWindow
from UIFiles.ui_holdings import Ui_holdings

from workers import HoldingsWorker

class TableModel(QAbstractTableModel):
    Ncol = None
    order = None

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    #essential to overide for custom header
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def sort(self, Ncol, order):
        """Sort table by given column number."""
        TableModel.Ncol = Ncol
        TableModel.order = order
        self.layoutAboutToBeChanged.emit()
        cols = self._data.columns
        self._data = self._data.sort_values(cols[TableModel.Ncol],
                                      ascending=TableModel.order == Qt.AscendingOrder)
        self.layoutChanged.emit()

class Holdings(QMainWindow):
    def __init__(self, parent=None):
        try:
            super().__init__(parent)
            self.ui = Ui_holdings()
            self.ui.setupUi(self)

            self.holdingsWorker = HoldingsWorker()
            self.holdingsThread = QThread()
            self.holdingsWorker.moveToThread(self.holdingsThread)

            self.holdingsWorker.isHoldingsPage = True
            self.holdingsThread.started.connect(self.holdingsWorker.getHoldingsTableModel)
            self.holdingsWorker.sigChngHoldData.connect(self.showHoldings)
            self.holdingsThread.start()
        except Exception as e:
            print(e)

    def closeEvent(self, event):
        print('closing holding window')
        self.holdingsWorker.isHoldingsPage = False
        TableModel.order = None
        TableModel.Ncol = None
        self.holdingsThread.quit()
        res = self.holdingsThread.wait()
        event.accept()
        print('called closeWindow', res)
    
    def closeWindow(self):
        self.close()
        
    def showHoldings(self, dfHoldings):
        model = TableModel(dfHoldings)
        if TableModel.order != None:
            model.sort(TableModel.Ncol, TableModel.order)
        self.ui.tvHoldings.setModel(model)
        