from PySide6.QtWidgets import QDialog, QHeaderView

from UIFiles.ui_messageDlg import Ui_dlgMessage

class MessageDlg(QDialog):
    def __init__(self, msg, parent=None):
        super().__init__(parent)
        self.ui = Ui_dlgMessage()
        self.ui.setupUi(self)
        self.ui.lblMsg.setText(msg)

        self.addConnectors()
    
    def addConnectors(self):
        self.ui.btnOk.clicked.connect(self.closeDlg)

    def close(self) -> bool:
        return super().close()

    def closeDlg(self):
        self.close()
