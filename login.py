# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
#
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.resize(392, 243)
        self.label = QtGui.QLabel(login)
        self.label.setGeometry(QtCore.QRect(140, 10, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 54, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txt_user = QtGui.QLineEdit(login)
        self.txt_user.setGeometry(QtCore.QRect(130, 50, 181, 29))
        self.txt_user.setObjectName(_fromUtf8("txt_user"))
        self.txt_pswd = QtGui.QLineEdit(login)
        self.txt_pswd.setGeometry(QtCore.QRect(130, 90, 181, 29))
        self.txt_pswd.setObjectName(_fromUtf8("txt_pswd"))
        self.btn_access = QtGui.QPushButton(login)
        self.btn_access.setGeometry(QtCore.QRect(170, 190, 85, 27))
        self.btn_access.setObjectName(_fromUtf8("btn_access"))
        self.btn_token = QtGui.QPushButton(login)
        self.btn_token.setGeometry(QtCore.QRect(160, 140, 101, 27))
        self.btn_token.setObjectName(_fromUtf8("btn_token"))

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        #self.btn_access.clicked.connect(self.login)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "Login ", None))
        self.label.setText(_translate("login", "Generador de Claves", None))
        self.label_2.setText(_translate("login", "Usuario", None))
        self.label_3.setText(_translate("login", "Contraseña", None))
        self.btn_access.setText(_translate("login", "Acceder", None))
        self.btn_token.setText(_translate("login", "generar token", None))

    