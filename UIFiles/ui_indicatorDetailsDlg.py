# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicatorDetailsDlg.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_dlgIndicatorDetails(object):
    def setupUi(self, dlgIndicatorDetails):
        if not dlgIndicatorDetails.objectName():
            dlgIndicatorDetails.setObjectName(u"dlgIndicatorDetails")
        dlgIndicatorDetails.resize(349, 234)
        self.verticalLayout = QVBoxLayout(dlgIndicatorDetails)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(dlgIndicatorDetails)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lblLen = QLabel(self.frame)
        self.lblLen.setObjectName(u"lblLen")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblLen)

        self.sbLen = QSpinBox(self.frame)
        self.sbLen.setObjectName(u"sbLen")
        self.sbLen.setMinimum(1)
        self.sbLen.setMaximum(10000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sbLen)

        self.lblWidth = QLabel(self.frame)
        self.lblWidth.setObjectName(u"lblWidth")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblWidth)

        self.dsbWidth = QDoubleSpinBox(self.frame)
        self.dsbWidth.setObjectName(u"dsbWidth")
        self.dsbWidth.setMaximum(10.000000000000000)
        self.dsbWidth.setValue(1.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dsbWidth)

        self.lblColor = QLabel(self.frame)
        self.lblColor.setObjectName(u"lblColor")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblColor)

        self.btnColor = QPushButton(self.frame)
        self.btnColor.setObjectName(u"btnColor")
        self.btnColor.setMaximumSize(QSize(30, 16777215))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.btnColor)

        self.lblName = QLabel(self.frame)
        self.lblName.setObjectName(u"lblName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblName)

        self.lblNameVal = QLabel(self.frame)
        self.lblNameVal.setObjectName(u"lblNameVal")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lblNameVal)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(dlgIndicatorDetails)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnOk = QPushButton(self.frame_2)
        self.btnOk.setObjectName(u"btnOk")

        self.horizontalLayout.addWidget(self.btnOk)

        self.btnDelete = QPushButton(self.frame_2)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnCancel = QPushButton(self.frame_2)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(dlgIndicatorDetails)

        QMetaObject.connectSlotsByName(dlgIndicatorDetails)
    # setupUi

    def retranslateUi(self, dlgIndicatorDetails):
        dlgIndicatorDetails.setWindowTitle(QCoreApplication.translate("dlgIndicatorDetails", u"Dialog", None))
        self.lblLen.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Length", None))
        self.lblWidth.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Width", None))
        self.lblColor.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Color", None))
        self.btnColor.setText("")
        self.lblName.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Name ", None))
        self.lblNameVal.setText(QCoreApplication.translate("dlgIndicatorDetails", u"TextLabel", None))
        self.btnOk.setText(QCoreApplication.translate("dlgIndicatorDetails", u"OK", None))
        self.btnDelete.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Delete", None))
        self.btnCancel.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Cancel", None))
    # retranslateUi

