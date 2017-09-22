# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelFrame.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500, 360)
        Form.setStyleSheet(_fromUtf8("background-image: url(:/img/Screenshot from 2017-09-20 17-37-17.png);"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 290, 75, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(29, 291, 75, 31))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 458, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"DejaVu Serif\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 330, 131, 20))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 italic 10pt \"URW Chancery L\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", "Sign In", None))
        self.pushButton.setText(_translate("Form", "Sign Up", None))
        self.label.setText(_translate("Form", "Welcome To Our Smart Garage", None))
        self.label_2.setText(_translate("Form", "Power By AIET Students", None))

import iamge_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

