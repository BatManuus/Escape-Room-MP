from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Main
from PyQt5.QtWidgets import QDialog
import mysql.connector as mc


class Ui_login_1(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, login_1):


        login_1.setObjectName("login_1")
        login_1.resize(801, 601)
        self.centralwidget = QtWidgets.QWidget(login_1)
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

        self.lresult = QtWidgets.QLabel(self.centralwidget)
        self.lresult.setGeometry(QtCore.QRect(210, 240, 171, 41))
        self.lresult.setObjectName("lresult")

        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(550, 250, 221, 31))
        self.username.setObjectName("username")
        
        self.password = QtWidgets.QLineEdit(self.centralwidget)
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

        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.clicked.connect(self.login)
        self.btn1.setGeometry(QtCore.QRect(610, 360, 91, 31))
        self.btn1.setObjectName("btn1")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("QPushButton {background-color : black ;color : white; }")


        
        login_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_1)
        QtCore.QMetaObject.connectSlotsByName(login_1)


    def login(self):
        try:
            username = self.username.text()
            password = self.password.text()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="chitta@12",
                database="login_1"
            )
            self.lresult.setText("Connected")
            mycursor = mydb.cursor()
        
            query = "SELECT username,password from login where username "" like '"+username +"' and password like '" + password + "'"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result == None:
                self.lresult.setText("Incorrect username or password")
            else:
                self.lresult.setText("Successfully logged in")
                login_1.close()
                self.openWindow()

        except mc.Error as e:
            self.lresult.setText("Error")
    

    def retranslateUi(self, login_1):
        _translate = QtCore.QCoreApplication.translate
        login_1.setWindowTitle(_translate("login_1", "Escape Room"))
        login_1.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.l1.setText(_translate("login_1", "Log-In"))
        self.l2.setText(_translate("login_1", "Username"))
        self.l3.setText(_translate("login_1", "Password"))
        self.btn1.setText(_translate("login_1", "Log-in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_1 = QtWidgets.QMainWindow()
    ui = Ui_login_1()
    ui.setupUi(login_1)
    login_1.show()
    sys.exit(app.exec_())
