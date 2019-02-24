#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from @crisantru
#
# WARNING! All changes made in this file will be lost!
import subprocess
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from Crypto.Cipher import AES
from Crypto import Random
import time
import datetime
import re

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(405, 448)

        # Variables globales
        self.password = ''
        self.registro_actual = 0
        self.key = b'Sixteen byte key0'	
        self.iv = Random.new().read(AES.block_size)

        self.tab_Keys = QtGui.QTabWidget(Dialog)
        self.tab_Keys.setGeometry(QtCore.QRect(0, 0, 561, 441))
        self.tab_Keys.setObjectName(_fromUtf8("tab_Keys"))

        self.tab_Generator = QtGui.QWidget()
        self.tab_Generator.setObjectName(_fromUtf8("tab_Generator"))

        self.chk_Mayus = QtGui.QCheckBox(self.tab_Generator)
        self.chk_Mayus.setGeometry(QtCore.QRect(20, 40, 191, 25))
        self.chk_Mayus.setObjectName(_fromUtf8("chk_Mayus"))
        self.label = QtGui.QLabel(self.tab_Generator)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.chk_Minus = QtGui.QCheckBox(self.tab_Generator)
        self.chk_Minus.setGeometry(QtCore.QRect(20, 70, 191, 25))
        self.chk_Minus.setObjectName(_fromUtf8("chk_Minus"))
        self.chk_Num = QtGui.QCheckBox(self.tab_Generator)
        self.chk_Num.setGeometry(QtCore.QRect(20, 100, 191, 25))
        self.chk_Num.setObjectName(_fromUtf8("chk_Num"))
        self.label_2 = QtGui.QLabel(self.tab_Generator)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 91, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_long = QtGui.QSpinBox(self.tab_Generator)
        self.txt_long.setGeometry(QtCore.QRect(120, 170, 113, 27))
        self.txt_long.setObjectName(_fromUtf8("txt_long"))
        self.txt_long.setRange(6, 20)
        self.txt_key = QtGui.QLineEdit(self.tab_Generator)
        self.txt_key.setGeometry(QtCore.QRect(170, 210, 201, 27))
        self.txt_key.setObjectName(_fromUtf8("txt_key"))
        self.txt_key.setReadOnly(True)
        self.btn_Start = QtGui.QPushButton(self.tab_Generator)
        self.btn_Start.setGeometry(QtCore.QRect(270, 170, 100, 27))
        self.btn_Start.setObjectName(_fromUtf8("btn_Start"))
        self.label_4 = QtGui.QLabel(self.tab_Generator)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 141, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_Save = QtGui.QPushButton(self.tab_Generator)
        self.btn_Save.setGeometry(QtCore.QRect(170, 270, 100, 27))
        self.btn_Save.setObjectName(_fromUtf8("btn_Save"))
        self.btn_close = QtGui.QPushButton(self.tab_Generator)
        self.btn_close.setGeometry(QtCore.QRect(280, 270, 100, 27))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.chk_Carac = QtGui.QCheckBox(self.tab_Generator)
        self.chk_Carac.setGeometry(QtCore.QRect(20, 130, 191, 25))
        self.chk_Carac.setObjectName(_fromUtf8("chk_Carac"))
        self.tab_Keys.addTab(self.tab_Generator, _fromUtf8(""))
        self.tab_Keys1 = QtGui.QWidget()
        self.tab_Keys1.setObjectName(_fromUtf8("tab_Keys1"))
        self.label_3 = QtGui.QLabel(self.tab_Keys1)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 76, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.tab_Keys1)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 101, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_Keys1)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 151, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_Keys1)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 151, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab_Keys1)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 111, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit = QtGui.QLineEdit(self.tab_Keys1)
        self.lineEdit.setGeometry(QtCore.QRect(180, 50, 201, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.txt_key2 = QtGui.QLineEdit(self.tab_Keys1)
        self.txt_key2.setGeometry(QtCore.QRect(180, 80, 201, 27))
        self.txt_key2.setObjectName(_fromUtf8("txt_key2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_Keys1)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 110, 201, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.txt_comentarios_tab2 = QtGui.QTextEdit(self.tab_Keys1)
        self.txt_comentarios_tab2.setGeometry(QtCore.QRect(180, 139, 201, 171))
        self.txt_comentarios_tab2.setObjectName(_fromUtf8("textEdit"))
        self.btn_Savetxt = QtGui.QPushButton(self.tab_Keys1)
        self.btn_Savetxt.setGeometry(QtCore.QRect(280, 320, 100, 27))
        self.btn_Savetxt.setObjectName(_fromUtf8("pushButton"))
        self.tab_Keys.addTab(self.tab_Keys1, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 201, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(40, 120, 151, 19))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(40, 150, 151, 19))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(40, 90, 101, 19))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(40, 60, 76, 19))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lbl_url = QtGui.QLineEdit(self.tab)
        self.lbl_url.setGeometry(QtCore.QRect(200, 120, 150, 19))
        self.lbl_url.setObjectName(_fromUtf8("lbl_url"))
        self.lbl_url.setReadOnly(True)
        self.lbl_pwd = QtGui.QLineEdit(self.tab)
        self.lbl_pwd.setGeometry(QtCore.QRect(200, 90, 150, 19))
        self.lbl_pwd.setObjectName(_fromUtf8("lbl_pwd"))
        self.lbl_pwd.setReadOnly(True)
        self.lbl_comm = QtGui.QTextEdit(self.tab)
        self.lbl_comm.setGeometry(QtCore.QRect(200, 150, 150, 191))
        self.lbl_comm.setObjectName(_fromUtf8("lbl_comm"))
        self.lbl_comm.setReadOnly(True)
        self.lbl_user = QtGui.QLineEdit(self.tab)
        self.lbl_user.setGeometry(QtCore.QRect(200, 60, 150, 19))
        self.lbl_user.setObjectName(_fromUtf8("lbl_user"))
        self.lbl_user.setReadOnly(True)
        self.btn_exportar = QtGui.QPushButton(self.tab)
        self.btn_exportar.setGeometry(QtCore.QRect(290, 360, 100, 27))
        self.btn_exportar.setObjectName(_fromUtf8("btn_exportar"))
        self.btn_sig = QtGui.QPushButton(self.tab)
        self.btn_sig.setGeometry(QtCore.QRect(160, 360, 100, 27))
        self.btn_sig.setObjectName(_fromUtf8("btn_sig"))
        self.btn_ant = QtGui.QPushButton(self.tab)
        self.btn_ant.setGeometry(QtCore.QRect(50, 360, 100, 27))
        self.btn_ant.setObjectName(_fromUtf8("btn_ant"))

        self.tab_Keys.addTab(self.tab, _fromUtf8(""))
        self.lbl_seguridad = QtGui.QLabel(self.tab_Generator)
        self.lbl_seguridad.setGeometry(QtCore.QRect(270, 240, 101, 20))
        self.lbl_seguridad.setObjectName(_fromUtf8("lbl_seguridad"))
        self.lbl_seguridad.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.retranslateUi(Dialog)
        self.tab_Keys.setCurrentIndex(0)
        self.ver_cont_init()

        # Eventos de botones
        self.btn_Start.clicked.connect(self.command)    #generar clave apartir de los atributos
        self.btn_Save.clicked.connect(self.sendKey)     #enviar clave a tab contraseñas
        self.btn_Savetxt.clicked.connect(self.saveTxt)  #guardar texto encriptado
        self.btn_sig.clicked.connect(self.siguienteRegistro)
        self.btn_ant.clicked.connect(self.anteriorRegistro)
        self.btn_close.clicked.connect(self.close)
        self.btn_exportar.clicked.connect(self.exportar)


        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Generador de Claves", None))
        self.chk_Mayus.setText(_translate("Dialog", "Letras Mayusculas", None))
        self.label.setText(_translate("Dialog", "Generador de Claves", None))
        self.chk_Minus.setText(_translate("Dialog", "Letras Minusculas", None))
        self.chk_Num.setText(_translate("Dialog", "Numeros", None))
        self.label_2.setText(_translate("Dialog", "Longitud", None))
        self.btn_Start.setText(_translate("Dialog", "Generar", None))
        self.label_4.setText(_translate("Dialog", "Clave Generada", None))
        self.btn_Save.setText(_translate("Dialog", "Guardar", None))
        self.btn_close.setText(_translate("Dialog", "Cerrar", None))
        self.chk_Carac.setText(_translate("Dialog", "Caracteres Especiales", None))
        self.tab_Keys.setTabText(self.tab_Keys.indexOf(self.tab_Generator), _translate("Dialog", "Generador", None))
        self.label_3.setText(_translate("Dialog", "Usuario", None))
        self.label_5.setText(_translate("Dialog", "Contraseña", None))
        self.label_6.setText(_translate("Dialog", "URL o Plataforma", None))
        self.label_7.setText(_translate("Dialog", "Comentarios", None))
        self.label_8.setText(_translate("Dialog", "Contraseñas", None))
        self.btn_Savetxt.setText(_translate("Dialog", "Guardar", None))
        self.tab_Keys.setTabText(self.tab_Keys.indexOf(self.tab_Keys1), _translate("Dialog", "Contraseñas", None))
        self.label_9.setText(_translate("Dialog", "Contraseñas Guardadas", None))
        self.label_11.setText(_translate("Dialog", "URL o Plataforma", None))
        self.label_12.setText(_translate("Dialog", "Comentarios", None))
        self.label_13.setText(_translate("Dialog", "Contraseña", None))
        self.label_14.setText(_translate("Dialog", "Usuario", None))
        self.btn_exportar.setText(_translate("Dialog", "Exportar", None))
        self.lbl_seguridad.setText(_translate("Dialog", "", None))
        self.btn_sig.setText(_translate("Dialog", "Siguiente", None))
        self.btn_ant.setText(_translate("Dialog", "Anterior", None))
        self.tab_Keys.setTabText(self.tab_Keys.indexOf(self.tab), _translate("Dialog", "Ver Contraseñas", None))


    def command(self):  #mandar comando terminal
       
        longitud = self.txt_long.value()
        command = 'pwgen ' + str(longitud)

        if not self.chk_Mayus.isChecked():
            command += ' -A'
        if not self.chk_Num.isChecked():
            command += ' -0'
        if self.chk_Carac.isChecked():
            command += ' -y'

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
	#print(output)

        self.password = str(output)
	#	print(self.password)
        self.password = self.password[2:-3]

        if self.chk_Mayus.isChecked() and not self.chk_Minus.isChecked():
            self.password = self.password.upper()

        self.txt_key.setText(self.password)

        nivel_seguridad = self.verificaSeguridad(self.password)

        if nivel_seguridad <= 2:
            self.lbl_seguridad.setStyleSheet('color: red')
            self.lbl_seguridad.setText('Débil')
        elif nivel_seguridad > 2 and nivel_seguridad <= 4:
            self.lbl_seguridad.setStyleSheet('color: #F44611')
            self.lbl_seguridad.setText('Moderado')
        else:
            self.lbl_seguridad.setStyleSheet('color: green')
            self.lbl_seguridad.setText('Fuerte')
        

    def sendKey(self):
        self.tab_Keys.setCurrentIndex(1)
        self.txt_key2.setText(self.password)
        self.chk_Mayus.setChecked(False)
        self.chk_Minus.setChecked(False)
        self.chk_Num.setChecked(False)
        self.chk_Carac.setChecked(False)
        self.txt_key.setText('')
        self.lbl_seguridad.setText('')
        self.txt_long.setValue(6)

    def saveTxt(self):
        if self.lineEdit.text() + self.txt_key2.text() + self.lineEdit_3.text() + self.txt_comentarios_tab2.toPlainText() == '':
            print('Nada que guardar')
            return

        txt = self.lineEdit.text() + ',' + self.txt_key2.text() + ',' + self.lineEdit_3.text() + ',' + self.txt_comentarios_tab2.toPlainText() + '\n' 
        #print(txt)
        try:
            file = open("password.lock", "a")
        except IOError:
            file = open("password.lock", "w")
       
        txt = txt.replace('ñ', '[n]')

        obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
        encrypted = str(obj.encrypt(txt))
        encrypted = encrypted[2:-1]

        file.write(str(encrypted) + '\n')
        file.close()
        self.lineEdit.setText('')
        self.txt_key2.setText('')
        self.lineEdit_3.setText('')
        self.txt_comentarios_tab2.setText('')
        self.ver_cont_init()

    def siguienteRegistro(self):
        try:
            file = open('password.lock', 'r')
            simpleText = file.readlines()
            self.registro_actual += 1

            if self.registro_actual >= len(simpleText):
                self.registro_actual = len(simpleText) - 1
                return

            obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')

            dec = simpleText[self.registro_actual].replace('\n', '')
            dec = bytes(dec, encoding='utf-8')
            dec = dec.decode('unicode-escape').encode('ISO-8859-1')

            mensaje_recuperado = str(obj2.decrypt(dec))
            mensaje_recuperado = mensaje_recuperado.replace('[n]', 'ñ')
            mensaje_recuperado = mensaje_recuperado.replace('\\\\', '\\')
            mensaje_recuperado = mensaje_recuperado[2:-3]
            mensaje_recuperado = mensaje_recuperado.split(',')

            self.lbl_user.setText(mensaje_recuperado[0])
            self.lbl_pwd.setText(mensaje_recuperado[1])
            self.lbl_url.setText(mensaje_recuperado[2])
            self.lbl_comm.setText(mensaje_recuperado[3])

            file.close()
        except IOError:
            print('No se pudo abrir el archivo')

    def anteriorRegistro(self):
        try:
            file = open('password.lock', 'r')
            simpleText = file.readlines()
            self.registro_actual -= 1

            if self.registro_actual < 0:
                self.registro_actual = 0
                return

            obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')

            dec = simpleText[self.registro_actual].replace('\n', '')
            dec = bytes(dec, encoding='utf-8')
            dec = dec.decode('unicode-escape').encode('ISO-8859-1')

            mensaje_recuperado = str(obj2.decrypt(dec))
            mensaje_recuperado = mensaje_recuperado.replace('[n]', 'ñ')
            mensaje_recuperado = mensaje_recuperado.replace('\\\\', '\\')
            mensaje_recuperado = mensaje_recuperado[2:-3]
            mensaje_recuperado = mensaje_recuperado.split(',')

            self.lbl_user.setText(mensaje_recuperado[0])
            self.lbl_pwd.setText(mensaje_recuperado[1])
            self.lbl_url.setText(mensaje_recuperado[2])
            self.lbl_comm.setText(mensaje_recuperado[3])

            file.close()
        except IOError:
            print('No se pudo abrir el archivo')           


    def ver_cont_init(self):
        try:
            file = open("password.lock", "r")
            simpleText = file.readlines(self.registro_actual)
            obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')

            dec = simpleText[0].replace("\n", '')
            dec = dec.replace('[n]', 'ñ')
            dec = bytes(dec, encoding='utf-8')
            dec = dec.decode('unicode-escape').encode('ISO-8859-1')

            mensaje_recuperado = str(obj2.decrypt(dec))
            mensaje_recuperado = mensaje_recuperado.replace('[n]', 'ñ')
            mensaje_recuperado = mensaje_recuperado.replace('\\\\', '\\')
            mensaje_recuperado = mensaje_recuperado[2:-3]
            mensaje_recuperado = mensaje_recuperado.split(',')

            self.lbl_user.setText(mensaje_recuperado[0])
            self.lbl_pwd.setText(mensaje_recuperado[1])
            self.lbl_url.setText(mensaje_recuperado[2])
            self.lbl_comm.setText(mensaje_recuperado[3])

            file.close()

        except IOError:
            self.lbl_user.setText('-')
            self.lbl_pwd.setText('-')
            self.lbl_url.setText('-')
            self.lbl_comm.setText('-')
    
    def exportar(self):

        usuario = self.lbl_user.text()
        cont = self.lbl_pwd.text()
        url = self.lbl_url.text()
        coment = self.lbl_comm.toPlainText()

        try:
            file_name = 'exportado' + datetime.datetime.now().strftime('%H:%M:%S') + '.txt'
            file = open(file_name, 'w')
            
            file.write('Usuario: ' + usuario + '\n')
            file.write('Contraseña: ' + cont + '\n')
            file.write('Url o Plataforma: ' + url + '\n')
            file.write('Comentarios: ' + coment + '\n')

            file.close()

            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setText('Exportado, archivo: ' + file_name)
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.setWindowTitle('Exportado')
            dialog.exec_()
        except IOError:
            print()

    def verificaSeguridad(self, password):
        # Calcula longitud de la contraseña
        longitud = len(password) < 8

        # Verifica si existen números
        digito = re.search(r"\d", password) is None

        # Verifica su hay mayúsculas
        minusculas = re.search(r"[A-Z]", password) is None

        # Verifica si hay minúsculas
        mayusculas = re.search(r"[a-z]", password) is None

        # Verifica si contiene símbolos
        simbolos = re.search(r"[ ;:@<>=¿?¡!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

        # Resultado
        #print(int(not longitud), int(not digito), int(not minusculas), int(not mayusculas), int(not simbolos))
        password_ok = int(not longitud) +  int(not digito) + int(not minusculas) + int(not mayusculas) + int(not simbolos)

        return password_ok

    def close(self):
        sys.exit(0)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    

