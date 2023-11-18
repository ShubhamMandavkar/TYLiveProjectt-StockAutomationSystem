# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alertDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_dlgAlert(object):
    def setupUi(self, dlgAlert):
        if not dlgAlert.objectName():
            dlgAlert.setObjectName(u"dlgAlert")
        dlgAlert.resize(473, 380)
        self.verticalLayout = QVBoxLayout(dlgAlert)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(dlgAlert)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblAlertType = QLabel(self.frame)
        self.lblAlertType.setObjectName(u"lblAlertType")

        self.gridLayout.addWidget(self.lblAlertType, 1, 0, 1, 1)

        self.sbLen1 = QSpinBox(self.frame)
        self.sbLen1.setObjectName(u"sbLen1")
        self.sbLen1.setMaximum(5000)

        self.gridLayout.addWidget(self.sbLen1, 5, 2, 1, 1)

        self.lblAlertMsg = QLabel(self.frame)
        self.lblAlertMsg.setObjectName(u"lblAlertMsg")

        self.gridLayout.addWidget(self.lblAlertMsg, 7, 0, 1, 1)

        self.lblAlertVal = QLabel(self.frame)
        self.lblAlertVal.setObjectName(u"lblAlertVal")

        self.gridLayout.addWidget(self.lblAlertVal, 4, 0, 1, 1)

        self.lblTimeFrame = QLabel(self.frame)
        self.lblTimeFrame.setObjectName(u"lblTimeFrame")

        self.gridLayout.addWidget(self.lblTimeFrame, 2, 0, 1, 1)

        self.lblAlertCond = QLabel(self.frame)
        self.lblAlertCond.setObjectName(u"lblAlertCond")

        self.gridLayout.addWidget(self.lblAlertCond, 3, 0, 1, 1)

        self.dsbAlertVal = QDoubleSpinBox(self.frame)
        self.dsbAlertVal.setObjectName(u"dsbAlertVal")
        self.dsbAlertVal.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.dsbAlertVal, 4, 2, 1, 1)

        self.cmbAlertType = QComboBox(self.frame)
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.setObjectName(u"cmbAlertType")

        self.gridLayout.addWidget(self.cmbAlertType, 1, 2, 1, 1)

        self.cmbAlertCond = QComboBox(self.frame)
        self.cmbAlertCond.addItem("")
        self.cmbAlertCond.addItem("")
        self.cmbAlertCond.setObjectName(u"cmbAlertCond")

        self.gridLayout.addWidget(self.cmbAlertCond, 3, 2, 1, 1)

        self.lblStkName = QLabel(self.frame)
        self.lblStkName.setObjectName(u"lblStkName")

        self.gridLayout.addWidget(self.lblStkName, 0, 0, 1, 1)

        self.leStkName = QLineEdit(self.frame)
        self.leStkName.setObjectName(u"leStkName")
        self.leStkName.setReadOnly(True)

        self.gridLayout.addWidget(self.leStkName, 0, 2, 1, 1)

        self.lblLen2 = QLabel(self.frame)
        self.lblLen2.setObjectName(u"lblLen2")

        self.gridLayout.addWidget(self.lblLen2, 6, 0, 1, 1)

        self.sbLen2 = QSpinBox(self.frame)
        self.sbLen2.setObjectName(u"sbLen2")
        self.sbLen2.setMaximum(5000)

        self.gridLayout.addWidget(self.sbLen2, 6, 2, 1, 1)

        self.txteMsg = QTextEdit(self.frame)
        self.txteMsg.setObjectName(u"txteMsg")

        self.gridLayout.addWidget(self.txteMsg, 7, 2, 1, 2)

        self.lblLen1 = QLabel(self.frame)
        self.lblLen1.setObjectName(u"lblLen1")

        self.gridLayout.addWidget(self.lblLen1, 5, 0, 1, 1)

        self.cmbTimeFrame = QComboBox(self.frame)
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.addItem("")
        self.cmbTimeFrame.setObjectName(u"cmbTimeFrame")

        self.gridLayout.addWidget(self.cmbTimeFrame, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.btnSetAlert = QPushButton(dlgAlert)
        self.btnSetAlert.setObjectName(u"btnSetAlert")

        self.verticalLayout.addWidget(self.btnSetAlert)


        self.retranslateUi(dlgAlert)

        QMetaObject.connectSlotsByName(dlgAlert)
    # setupUi

    def retranslateUi(self, dlgAlert):
        dlgAlert.setWindowTitle(QCoreApplication.translate("dlgAlert", u"Dialog", None))
        self.lblAlertType.setText(QCoreApplication.translate("dlgAlert", u"Type", None))
        self.lblAlertMsg.setText(QCoreApplication.translate("dlgAlert", u"Message", None))
        self.lblAlertVal.setText(QCoreApplication.translate("dlgAlert", u"Value", None))
        self.lblTimeFrame.setText(QCoreApplication.translate("dlgAlert", u"Time Frame", None))
        self.lblAlertCond.setText(QCoreApplication.translate("dlgAlert", u"Condition", None))
        self.cmbAlertType.setItemText(0, QCoreApplication.translate("dlgAlert", u"Price", None))
        self.cmbAlertType.setItemText(1, QCoreApplication.translate("dlgAlert", u"MA", None))
        self.cmbAlertType.setItemText(2, QCoreApplication.translate("dlgAlert", u"Price + EMA", None))
        self.cmbAlertType.setItemText(3, QCoreApplication.translate("dlgAlert", u"Price + HMA", None))

        self.cmbAlertCond.setItemText(0, QCoreApplication.translate("dlgAlert", u"Greater Than", None))
        self.cmbAlertCond.setItemText(1, QCoreApplication.translate("dlgAlert", u"Less Than", None))

        self.lblStkName.setText(QCoreApplication.translate("dlgAlert", u"Stock Name", None))
        self.lblLen2.setText(QCoreApplication.translate("dlgAlert", u"Length2", None))
        self.lblLen1.setText(QCoreApplication.translate("dlgAlert", u"Length1", None))
        self.cmbTimeFrame.setItemText(0, QCoreApplication.translate("dlgAlert", u"Daily", None))
        self.cmbTimeFrame.setItemText(1, QCoreApplication.translate("dlgAlert", u"Weekly", None))
        self.cmbTimeFrame.setItemText(2, QCoreApplication.translate("dlgAlert", u"Monthly", None))

        self.btnSetAlert.setText(QCoreApplication.translate("dlgAlert", u"set Alert", None))
    # retranslateUi

