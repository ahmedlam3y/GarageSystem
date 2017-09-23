import sys
from PyQt4.QtGui import QWidget, QApplication

from SignIN import Ui_Form as SignInForm
from WelFrame import Ui_Form as WelFrameForm
from SignUp import Ui_Form as SignUpForm
from Accounting import Ui_Form as AccountForm


class SignIn(QWidget, SignInForm):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


class WelFrame(QWidget, WelFrameForm):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.move(300, 200)


class SignUp(QWidget, SignUpForm):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


class Accout(QWidget, AccountForm):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


def foo(w1, w2):
    w1.show()
    w1.move(300, 200)
    w2.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
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
