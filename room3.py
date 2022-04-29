from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QPushButton,QWidget

#####Physics
class Ui_room3(QWidget):
    def setupUi(self, room3):
        room3.setObjectName("room3")
        room3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(room3)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\gorug\\PycharmProjects\\EscapeRoom-MP\\images\\room_4.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 160, 135, 360))
        self.pushButton.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton.setObjectName("")
        self.pushButton.clicked.connect(self.show_dialog)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 210, 81, 21))
        self.pushButton_2.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_2.setObjectName("")
        self.pushButton_2.clicked.connect(self.show_dialog_1)
       
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 120, 120, 40))
        self.pushButton_3.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_3.setObjectName("")
        self.pushButton_3.clicked.connect(self.show_dialog_2)
      
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(670, 270, 143, 58))
        self.pushButton_4.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_4.setObjectName("")
        self.pushButton_4.clicked.connect(self.show_dialog_3)
       
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_5.setGeometry(QtCore.QRect(350, 150, 83, 128))
        self.pushButton_5.setObjectName("")
        self.pushButton_5.clicked.connect(self.show_dialog_4)

        room3.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(room3)
        QtCore.QMetaObject.connectSlotsByName(room3)

    def retranslateUi(self, room3):
        _translate = QtCore.QCoreApplication.translate
        room3.setWindowTitle(_translate("room3", "room3"))
        self.pushButton.setText(_translate("room3", ""))
        self.pushButton_2.setText(_translate("room3", ""))
        self.pushButton_3.setText(_translate("room3", ""))
        self.pushButton_4.setText(_translate("room3", ""))
        self.pushButton_5.setText(_translate("room3", ""))

    def show_dialog(self, room3):
        text, ok = QInputDialog.getText(self, 'Exit ', 'Enter The Code In Same Order:')
        print(text)
        print (ok)


    def show_dialog_1(self, room3):
        text, ok = QInputDialog.getText(self, 'Hint Number 1', '1.Helium shows Bose-Einstein condensation below what temperature? (in K)')
        print(text)
        print (ok)

    def show_dialog_2(self, room3):
        text, ok = QInputDialog.getText(self, 'Hint Number 2', '2.The water droplets in free fall are spherical due to:')
        print(text)
        print (ok)


    def show_dialog_3(self, room3):
        text, ok = QInputDialog.getText(self, 'Hint Number 3', '3.Which component of linear momentum does not contribute to angular momentum?')
        print(text)
        print (ok)


    def show_dialog_4(self, room3):
        text, ok = QInputDialog.getText(self, 'Hint Number 4', '4.If an object reaches the speed of light, its length changes to')
        print(text)
        print (ok)

    def retranslateUi(self, room3):
        _translate = QtCore.QCoreApplication.translate
        room3.setWindowTitle(_translate("room3","Escape Room"))
        room3.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    room3 = QtWidgets.QMainWindow()
    ui = Ui_room3()
    ui.setupUi(room3)
    room3.show()
    sys.exit(app.exec_())
