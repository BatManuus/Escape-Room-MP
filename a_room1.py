from PyQt5 import QtCore, QtGui, QtWidgets,QtDesigner
from PyQt5.QtWidgets import QInputDialog,QPushButton,QWidget


class Ui_room1(QWidget):
    def openWindow(self):
        from corridor import Ui_corridor
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_corridor()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, room1):
        room1.setObjectName("Room_2")
        room1.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        room1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(room1)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/room1.png"))
        self.label.setObjectName("label")
        
        self.clue1 = QtWidgets.QPushButton(self.centralwidget)
        self.clue1.setGeometry(QtCore.QRect(610, 202, 71, 111))
        self.clue1.setText("")
        self.clue1.setStyleSheet("QPushButton{background: transparent;}")
        self.clue1.setObjectName("pushButton")
        self.clue1.clicked.connect(self.show_dialog_1)

        self.clue2 = QtWidgets.QPushButton(self.centralwidget)
        self.clue2.setGeometry(QtCore.QRect(230, 80, 71, 111))
        self.clue2.setText("")
        self.clue2.setStyleSheet("QPushButton{background: transparent;}")
        self.clue2.setObjectName("pushButton")
        self.clue2.clicked.connect(self.show_dialog_2)

        self.clue3 = QtWidgets.QPushButton(self.centralwidget)
        self.clue3.setGeometry(QtCore.QRect(440, 70, 71, 111))
        self.clue3.setText("")
        self.clue3.setStyleSheet("QPushButton{background: transparent;}")
        self.clue3.setObjectName("pushButton")
        self.clue3.clicked.connect(self.show_dialog_3)
       
        self.clue4 = QtWidgets.QPushButton(self.centralwidget)
        self.clue4.setGeometry(QtCore.QRect(125, 350, 90, 45))
        self.clue4.setText("")
        self.clue4.setStyleSheet("QPushButton{background: transparent;}")
        self.clue4.setObjectName("pushButton")
        self.clue4.clicked.connect(self.show_dialog_4)
     
        self.door = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.door.clicked.connect(room1.close)
        self.door.setGeometry(QtCore.QRect(0, 0, 80, 500))
        self.door.setText("")
        self.door.setStyleSheet("QPushButton{background: transparent;}")
        self.door.setObjectName("pushButton")
        self.door.clicked.connect(self.show_dialog)


        room1.setCentralWidget(self.centralwidget)

        self.retranslateUi(room1)
        QtCore.QMetaObject.connectSlotsByName(room1)

    def show_dialog(self, room1):
        text, ok = QInputDialog.getText(self, 'Exit ', 'Enter The Code In Same Order:')
        print(text)
        print (ok)


    def show_dialog_1(self, room1):
        text, ok = QInputDialog.getText(self, 'Hint Number 1', '1.What is data about data called?:')
        print(text)
        print (ok)

    def show_dialog_2(self, room1):
        text, ok = QInputDialog.getText(self, 'Hint Number 2', '2.What level of data abstraction describes exactly how the data actually stored?')
        print(text)
        print (ok)


    def show_dialog_3(self, room1):
        text, ok = QInputDialog.getText(self, 'Hint Number 3', '3.What refers to the number of tuples in a relation?')
        print(text)
        print (ok)


    def show_dialog_4(self, room1):
        text, ok = QInputDialog.getText(self, 'Hint Number 4', '4.Which command is used to restore the database to the last committed state?')
        print(text)
        print (ok)

    def retranslateUi(self, room1):
        _translate = QtCore.QCoreApplication.translate
        room1.setWindowTitle(_translate("room1", "Escape Room"))
        room1.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    room1 = QtWidgets.QMainWindow()
    ui = Ui_room1()
    ui.setupUi(room1)
    room1.show()
    sys.exit(app.exec_())


