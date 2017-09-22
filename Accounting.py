# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accounting.ui'
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
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 9, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 7, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 9, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 9, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_5.setText(_translate("Form", "Your Cost Now", None))
        self.label_6.setText(_translate("Form", "Operation", None))
        self.pushButton.setText(_translate("Form", "Change Data", None))
        self.label_3.setText(_translate("Form", "Car Color", None))
        self.comboBox.setItemText(0, _translate("Form", "Car IN", None))
        self.comboBox.setItemText(1, _translate("Form", "Car OUT", None))
        self.label_4.setText(_translate("Form", "Time Use", None))
        self.label.setText(_translate("Form", "Car Number", None))
        self.label_2.setText(_translate("Form", "Car Model", None))
        self.pushButton_2.setText(_translate("Form", "Exit", None))
        self.pushButton_3.setText(_translate("Form", "OK", None))

import iamge_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form=Form)
    Form.show()
    sys.exit(app.exec_())

