import sys
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets as Q
from PyQt5.QtGui import QImage, QPalette, QBrush

import image_rc
from SignIN import Ui_Form as SignInForm
from WelFrame import Ui_Form as WelFrameForm
from SignUp import Ui_Form as SignUpForm
from Accounting import Ui_Form as AccountForm


class SignIn(Q.QWidget, SignInForm):  # Widget
    def __init__(self, parent=None):
        super(SignIn, self).__init__(parent)
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


class WelFrame(Q.QWidget, WelFrameForm):  # MainWindow
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)
        self.move(300, 200)


class SignUp(Q.QWidget, SignUpForm):  # Widget
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


class Accout(Q.QWidget, AccountForm):  # Widget
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


def foo(w1, w2):
    w1.show()
    w1.move(300, 200)
    w2.hide()


if __name__ == '__main__':
    app = Q.QApplication(sys.argv)
    wel = WelFrame()
    signIn = SignIn()
    signUp = SignUp()
    accout = AccountForm()
    wel.pushButton_2.clicked.connect(lambda: foo(signIn, wel))
    wel.pushButton.clicked.connect(lambda: foo(signUp, wel))
    signIn.pushButton_2.clicked.connect(lambda: foo(wel, signIn))
    signUp.pushButton_2.clicked.connect(lambda: foo(wel, signUp))
    wel.show()
    sys.exit(app.exec_())
