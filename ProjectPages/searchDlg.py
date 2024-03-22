from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QDialog, QHeaderView

import pandas as pd
import mysql.connector
from mysql.connector import errorcode
from UIFiles.ui_searchDialog import Ui_dlgSearch


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        return None

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
        self.layoutAboutToBeChanged.emit()
        cols = self._data.columns
        self._data = self._data.sort_values(cols[Ncol],
                                      ascending=order == Qt.AscendingOrder)
        self.layoutChanged.emit()


class SearchDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgSearch()
        self.ui.setupUi(self)
        self.setWindowTitle('Search')

        self.ui.tblvSuggestions.horizontalHeader().setStretchLastSection(True)
        self.ui.tblvSuggestions.horizontalHeader().setDefaultSectionSize(200)
        # self.ui.tblvSuggestions.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.addConnectors()
        self.showSuggestions()
    
    def addConnectors(self):
        self.ui.leSearch.textChanged.connect(self.showSuggestions)

    def showSuggestions(self):
        stkSym = self.ui.leSearch.text()
        try:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "123456", database='ty_live_proj_stock_automation_sys')
            cursor = con.cursor()

            #get the value of stkSymbol
            query = f"""select * from stocks where stkSymbol like '{stkSym}%'"""
            cursor.execute(query)

            data = {'Symbol':[], 'Name':[]}
            for symbol,name, *_ in cursor: #cursor returns tuple
                data['Symbol'].append(symbol)
                data['Name'].append(name)

            data = pd.DataFrame(data)
            model = TableModel(data)    
            self.ui.tblvSuggestions.setModel(model) 

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("error:",err)
        finally:
            cursor.close()
            con.close()
