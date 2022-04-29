from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_corridor(object):
    def openWindow(self):
        from a_room1 import Ui_room1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room1()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow1(self):
        from b_room2 import Ui_room2 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        from c_room3 import Ui_room3 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room3()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow3(self):
        from d_room4 import Ui_room4
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_room4()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, corridor):
        corridor.setObjectName("corridor")
        corridor.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(corridor)
        self.centralwidget.setObjectName("centralwidget")
        
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/corridor.png")) 
        self.bg.setObjectName("bg")
        
        self.room_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.room_1.clicked.connect(corridor.close)
        self.room_1.setGeometry(QtCore.QRect(290, 70, 51, 441))
        self.room_1.setText("")
        self.room_1.setStyleSheet("QPushButton{background: transparent;}")
        self.room_1.setObjectName("room_1")
        
        self.room_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow1())
        self.room_2.clicked.connect(corridor.close)
        self.room_2.setGeometry(QtCore.QRect(700, -10, 151, 611))
        self.room_2.setText("")
        self.room_2.setStyleSheet("QPushButton{background: transparent;}")
        self.room_2.setObjectName("room_2")
        
        self.room_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow2())
        self.room_3.clicked.connect(corridor.close)
        self.room_3.setGeometry(QtCore.QRect(550, 40, 51, 471))
        self.room_3.setText("")
        self.room_3.setStyleSheet("QPushButton{background: transparent;}")
        self.room_3.setObjectName("room_3")
        
        self.room_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow3())
        self.room_4.clicked.connect(corridor.close)
        self.room_4.setGeometry(QtCore.QRect(360, 150, 41, 301))
        self.room_4.setText("")
        self.room_4.setObjectName("room_4")
        self.room_4.setStyleSheet("QPushButton{background: transparent;}")
        corridor.setCentralWidget(self.centralwidget)

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.clicked.connect(corridor.close)
        self.exit.setGeometry(QtCore.QRect(410, 210, 91, 181))
        self.exit.setText("")
        self.exit.setStyleSheet("QPushButton{background: transparent;}")
        self.exit.setObjectName("exit")

        self.retranslateUi(corridor)
        QtCore.QMetaObject.connectSlotsByName(corridor)

    def retranslateUi(self, corridor):
        _translate = QtCore.QCoreApplication.translate
        corridor.setWindowTitle(_translate("corridor","Escape Room"))
        corridor.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    corridor = QtWidgets.QMainWindow()
    ui = Ui_corridor()
    ui.setupUi(corridor)
    corridor.show()
    sys.exit(app.exec_())
