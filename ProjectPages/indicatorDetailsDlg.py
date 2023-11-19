from PySide6.QtWidgets import QDialog
from UIFiles.ui_indicatorDetailsDlg import Ui_dlgIndicatorDetails

class IndicatorDetailsDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgIndicatorDetails()
        self.ui.setupUi(self)