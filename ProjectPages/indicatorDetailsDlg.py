import PySide6.QtGui
from PySide6.QtWidgets import QDialog, QColorDialog
from UIFiles.ui_indicatorDetailsDlg import Ui_dlgIndicatorDetails

class IndicatorDetailsDlg(QDialog):
    def __init__(self, name = '', color = 'blue', parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgIndicatorDetails()
        self.ui.setupUi(self)
        self.setWindowTitle('Indicator Details')

        self.ui.btnDelete.hide()
        self.ui.lblNameVal.setText(name)

        self.colorDlg = QColorDialog()
        self.colorDlg.setCurrentColor(color)
        self.color = self.colorDlg.currentColor()
        self.ui.btnColor.setStyleSheet(f"background-color: { self.color.name() }")
        self.addConnectors()

    def addConnectors(self):
        self.ui.btnOk.clicked.connect(self.closeDlg)
        self.ui.btnCancel.clicked.connect(self.closeDlg)
        self.ui.btnDelete.clicked.connect(self.closeDlg)

        self.ui.btnColor.clicked.connect(self.colorDlg.show)
        self.colorDlg.colorSelected.connect(self.setColor)

    def setColor(self):
        self.color = self.colorDlg.currentColor()
        self.ui.btnColor.setStyleSheet(f"background-color: {self.color.name()};")
    
    def closeEvent(self, arg__1: PySide6.QtGui.QCloseEvent) -> None:
        self.colorDlg.close()
        return super().closeEvent(arg__1)

    def closeDlg(self):
        self.colorDlg.close()
        self.close()

