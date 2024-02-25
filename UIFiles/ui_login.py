# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1027, 576)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(700, 416))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 63, 20))

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 60))
        self.label.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lblUserName = QLabel(self.frame_3)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setMinimumSize(QSize(0, 20))
        self.lblUserName.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.lblUserName, 1, 0, 1, 1)

        self.leUserName = QLineEdit(self.frame_3)
        self.leUserName.setObjectName(u"leUserName")
        self.leUserName.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.leUserName, 2, 0, 1, 1)

        self.lblPassword = QLabel(self.frame_3)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setMinimumSize(QSize(0, 20))
        self.lblPassword.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.lblPassword, 3, 0, 1, 1)

        self.lePassword = QLineEdit(self.frame_3)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMaximumSize(QSize(16777215, 40))
        self.lePassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lePassword, 4, 0, 1, 1)

        self.btnLogin = QPushButton(self.frame_3)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.btnLogin, 5, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1027, 25))
        Login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.lblUserName.setText(QCoreApplication.translate("Login", u"Username", None))
        self.lblPassword.setText(QCoreApplication.translate("Login", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

