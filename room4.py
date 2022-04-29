from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QPushButton,QWidget


class Ui_room4(QWidget):
    def setupUi(self, room4):
        room4.setObjectName("room4")
        room4.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(room4)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/room_3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 172, 100, 220))
        self.pushButton.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton.setObjectName("")
        self.pushButton.clicked.connect(self.show_dialog)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 442, 81, 31))
        self.pushButton_2.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_2.setObjectName("")
        self.pushButton_2.clicked.connect(self.show_dialog_1)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 230, 81, 31))
        self.pushButton_3.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_3.setObjectName("")
        self.pushButton_3.clicked.connect(self.show_dialog_2)

        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_4.setGeometry(QtCore.QRect(320, 332, 81, 31))
        self.pushButton_4.setObjectName("")
        self.pushButton_4.clicked.connect(self.show_dialog_3)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 512, 81, 31))
        self.pushButton_5.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton_5.setObjectName("")
        self.pushButton_5.clicked.connect(self.show_dialog_4)

        room4.setCentralWidget(self.centralwidget)

        self.retranslateUi(room4)
        QtCore.QMetaObject.connectSlotsByName(room4)

    def show_dialog(self, room4):
        text, ok = QInputDialog.getText(self, 'Exit ', 'Enter The Code In Same Order:')
        print(text)
        print (ok)


    def show_dialog_1(self, room4):
        text, ok = QInputDialog.getText(self, 'Hint Number 1', '1.What is the hybridisation of C in CO32-')
        print(text)
        print (ok)

    def show_dialog_2(self, room4):
        text, ok = QInputDialog.getText(self, 'Hint Number 2', '2.Orlon is a polymer of?')
        print(text)
        print (ok)


    def show_dialog_3(self, room4):
        text, ok = QInputDialog.getText(self, 'Hint Number 3', '3.What name reaction reduces ketones or aldehydes using zinc amalgam and HCL?')
        print(text)
        print (ok)


    def show_dialog_4(self, room4):
        text, ok = QInputDialog.getText(self, 'Hint Number 4', '4.What is the hybridisation of P in PF5?')
        print(text)
        print (ok)


    def retranslateUi(self, room4):
        _translate = QtCore.QCoreApplication.translate
        room4.setWindowTitle(_translate("room4", "Escape Room"))
        room4.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.pushButton.setText(_translate("room4", ""))
        self.pushButton_2.setText(_translate("room4", ""))
        self.pushButton_3.setText(_translate("room4", ""))
        self.pushButton_4.setText(_translate("room4", ""))
        self.pushButton_5.setText(_translate("room4", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    room4 = QtWidgets.QMainWindow()
    ui = Ui_room4()
    ui.setupUi(room4)
    room4.show()
    sys.exit(app.exec_())
