from PySide6.QtWidgets import QDialog
from UIFiles.ui_watchlistDetailsDlg import Ui_watchlistDetails

class WatchlistDetailsDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_watchlistDetails()
        self.ui.setupUi(self)

        self.addConnectors()
    
    def addConnectors(self):
        self.ui.btnCancel.clicked.connect(lambda:self.close())
    
