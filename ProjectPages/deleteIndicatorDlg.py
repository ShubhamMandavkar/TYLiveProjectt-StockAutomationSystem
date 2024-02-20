from PySide6.QtWidgets import QDialog
from UIFiles.ui_deleteIndicatorDlg import Ui_dlgDeleteIndicator

class DeleteIndicatorDlg(QDialog):
    isDeleted = False
    def __init__(self, name, length, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgDeleteIndicator()
        self.ui.setupUi(self)
        self.setWindowTitle('Indicator Details')

        self.indicatorName = name
        self.length = length

        self.showDetails()

    def showDetails(self):
        self.ui.lblIndicatorName.setText(self.indicatorName)
        self.ui.lblLenVal.setText(str(self.length))
