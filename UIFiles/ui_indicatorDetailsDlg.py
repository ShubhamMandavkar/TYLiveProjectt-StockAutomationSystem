# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicatorDetailsDlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QLabel, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_dlgIndicatorDetails(object):
    def setupUi(self, dlgIndicatorDetails):
        if not dlgIndicatorDetails.objectName():
            dlgIndicatorDetails.setObjectName(u"dlgIndicatorDetails")
        dlgIndicatorDetails.resize(349, 146)
        self.verticalLayout = QVBoxLayout(dlgIndicatorDetails)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(dlgIndicatorDetails)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.sbLen = QSpinBox(self.frame)
        self.sbLen.setObjectName(u"sbLen")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sbLen)

        self.lblLen = QLabel(self.frame)
        self.lblLen.setObjectName(u"lblLen")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblLen)


        self.verticalLayout.addWidget(self.frame)

        self.bbOkCancel = QDialogButtonBox(dlgIndicatorDetails)
        self.bbOkCancel.setObjectName(u"bbOkCancel")
        self.bbOkCancel.setOrientation(Qt.Horizontal)
        self.bbOkCancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bbOkCancel.setCenterButtons(False)

        self.verticalLayout.addWidget(self.bbOkCancel)


        self.retranslateUi(dlgIndicatorDetails)
        self.bbOkCancel.accepted.connect(dlgIndicatorDetails.accept)
        self.bbOkCancel.rejected.connect(dlgIndicatorDetails.reject)

        QMetaObject.connectSlotsByName(dlgIndicatorDetails)
    # setupUi

    def retranslateUi(self, dlgIndicatorDetails):
        dlgIndicatorDetails.setWindowTitle(QCoreApplication.translate("dlgIndicatorDetails", u"Dialog", None))
        self.lblLen.setText(QCoreApplication.translate("dlgIndicatorDetails", u"Length", None))
    # retranslateUi

