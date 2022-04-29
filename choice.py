from PyQt5 import QtCore, QtGui, QtWidgets
from room1 import Ui_room1
from room2 import Ui_room2
from room3 import Ui_room3
from room4 import Ui_room4




class Ui_choice(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room1()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room3()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room4()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow4(self):
        from menu import Ui_menu
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, choice):
        choice.setObjectName("choice")
        choice.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(choice)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/bg_1.png"))
        self.bg.setObjectName("bg")
       
        self.room1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow2())
        self.room1.setGeometry(QtCore.QRect(50, 160, 151, 301))
        self.room1.clicked.connect(choice.close)
        self.room1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/math_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.room1.setIcon(icon)
        self.room1.setIconSize(QtCore.QSize(150, 301))
        self.room1.setObjectName("room1")
       
        self.room2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow3())
        self.room2.clicked.connect(choice.close)
        self.room2.setGeometry(QtCore.QRect(240, 160, 151, 301))
        self.room2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/chem_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.room2.setIcon(icon1)
        self.room2.setIconSize(QtCore.QSize(150, 301))
        self.room2.setObjectName("room2")
       
        self.room3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow1())
        self.room3.clicked.connect(choice.close)
        self.room3.setGeometry(QtCore.QRect(430, 160, 151, 301))
        self.room3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/prog_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.room3.setIcon(icon2)
        self.room3.setIconSize(QtCore.QSize(150, 301))
        self.room3.setObjectName("room3")
       
        self.room4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.room4.clicked.connect(choice.close)
        self.room4.setGeometry(QtCore.QRect(610, 160, 151, 301))
        self.room4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/dbms_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.room4.setIcon(icon3)
        self.room4.setIconSize(QtCore.QSize(150, 301))
        self.room4.setObjectName("room4")

        self.back = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow4())
        self.back.clicked.connect(choice.close)
        self.back.setGeometry(QtCore.QRect(20, 20, 91, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon2)
        self.back.setIconSize(QtCore.QSize(150, 45))
        self.back.setObjectName("back")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(56, 28, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel {color : white; }")
        


       
        choice.setCentralWidget(self.centralwidget)

        self.retranslateUi(choice)
        QtCore.QMetaObject.connectSlotsByName(choice)

    def retranslateUi(self, choice):
        _translate = QtCore.QCoreApplication.translate
        choice.setWindowTitle(_translate("choice", "Escape Room"))
        choice.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.label_3.setText(_translate("choice", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    choice = QtWidgets.QMainWindow()
    ui = Ui_choice()
    ui.setupUi(choice)
    choice.show()
    sys.exit(app.exec_())
