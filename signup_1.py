from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
from login_1 import Ui_login_1


class Ui_signup_1(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_login_1()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, signup_1):
        signup_1.setObjectName("signup_1")
        signup_1.resize(801, 601)
        self.centralwidget = QtWidgets.QWidget(signup_1)
        self.centralwidget.setObjectName("centralwidget")
        
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/login_1.png"))
        self.bg.setObjectName("bg")
        
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(540, 140, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.l1.setStyleSheet("QLabel {color : white; }")
        
        self.user = QtWidgets.QTextEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(550, 250, 221, 31))
        self.user.setObjectName("user")
        
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(550, 300, 221, 31))
        self.password.setObjectName("password")
        
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(450, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.l2.setStyleSheet("QLabel {color : white; }")
        
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(450, 310, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.l3.setStyleSheet("QLabel {color : white; }")

        
        self.btn = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.btn.clicked.connect(signup_1.close)
        self.btn.setGeometry(QtCore.QRect(560, 360, 91, 31))
        self.btn.setObjectName("btn")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setStyleSheet("QPushButton {background-color : black ;color : white; }")
        
        self.btn1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.btn1.clicked.connect(signup_1.close)
        self.btn1.setGeometry(QtCore.QRect(660, 360, 91, 31))
        self.btn1.setObjectName("btn1")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("QPushButton {background-color : black ;color : white; }")
        
        signup_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(signup_1)
        QtCore.QMetaObject.connectSlotsByName(signup_1)

    def retranslateUi(self, signup_1):
        _translate = QtCore.QCoreApplication.translate
        signup_1.setWindowTitle(_translate("signup_1", "Escape Room"))
        signup_1.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.l1.setText(_translate("signup_1", "Sign-Up"))
        self.l2.setText(_translate("signup_1", "User"))
        self.l3.setText(_translate("signup_1", "Password"))
        self.btn.setText(_translate("signup_1", "Sign-up"))
        self.btn1.setText(_translate("signup_1", "Log-in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signup_1 = QtWidgets.QMainWindow()
    ui = Ui_signup_1()
    ui.setupUi(signup_1)
    signup_1.show()
    sys.exit(app.exec_())
