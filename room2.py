from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QPushButton,QWidget


#####Coding
class Ui_room2(QWidget):
    
    def setupUi(self, room2):
        room2.setObjectName("room2")
        room2.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        room2.setFont(font)
        self.centralwidget = QtWidgets.QWidget(room2)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/room_2.png"))
        self.label.setObjectName("label")
        
        self.door = QtWidgets.QPushButton(self.centralwidget)
        self.door.setGeometry(QtCore.QRect(560, 160, 101, 201))
        self.door.setText("")
        self.door.setStyleSheet("QPushButton{background: transparent;}")
        self.door.clicked.connect(self.show_dialog)
        self.door.setObjectName("door")
       
        self.clue1 = QtWidgets.QPushButton(self.centralwidget)
        self.clue1.setGeometry(QtCore.QRect(370, 390, 161, 141))
        self.clue1.setText("")
        self.clue1.setStyleSheet("QPushButton{background: transparent;}")
        self.clue1.clicked.connect(self.show_dialog_1)
        self.clue1.setObjectName("clue1")
        
        self.clue2 = QtWidgets.QPushButton(self.centralwidget)
        self.clue2.setGeometry(QtCore.QRect(300, 180, 81, 80))
        self.clue2.setText("")
        self.clue2.setStyleSheet("QPushButton{background: transparent;}")
        self.clue2.clicked.connect(self.show_dialog_2)
        self.clue2.setObjectName("clue2")
        
        self.clue3 = QtWidgets.QPushButton(self.centralwidget)
        self.clue3.setGeometry(QtCore.QRect(90, 252, 181, 151))
        self.clue3.setText("")
        self.clue3.setStyleSheet("QPushButton{background: transparent;}")
        self.clue3.clicked.connect(self.show_dialog_3)
        self.clue3.setObjectName("clue3")
        
        self.clue4 = QtWidgets.QPushButton(self.centralwidget)
        self.clue4.setGeometry(QtCore.QRect(400, 160, 71, 61))
        self.clue4.setText("")
        self.clue4.setStyleSheet("QPushButton{background: transparent;}")
        self.clue4.clicked.connect(self.show_dialog_4)
        self.clue4.setObjectName("clue4")
       
        room2.setCentralWidget(self.centralwidget)

        self.retranslateUi(room2)
        QtCore.QMetaObject.connectSlotsByName(room2)
    
    def show_dialog(self,room2):
        text, ok = QInputDialog.getText(self, 'Exit', 'Put The Number In The Same Order:')
        print(text)
        print (ok)
    
    def show_dialog_1(self,room2):
        text, ok = QInputDialog.getText(self, 'Hint Number 1', '1.What is the return type of the hashCode() method in the Object class?')
        print(text)
        print (ok)

    def show_dialog_2(self,room2):
        text, ok = QInputDialog.getText(self, 'Hint Number 2', '2.In which process, a local variable has the same name as one of the instance variables?')
        print(text)
        print (ok)

    def show_dialog_3(self,room2):
        text, ok = QInputDialog.getText(self, 'Hint Number 3', '3.In which memory a String is stored, when we create a string using new operator?')
        print(text)
        print (ok)

    def show_dialog_4(self,room2):
        text, ok = QInputDialog.getText(self, 'Hint Number 4', '4.Hiding internal details and showing functionality is known as what?')
        print(text)
        print (ok)

    def retranslateUi(self, room2):
        _translate = QtCore.QCoreApplication.translate
        room2.setWindowTitle(_translate("room2", "Escape Room"))
        room2.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    room2 = QtWidgets.QMainWindow()
    ui = Ui_room2()
    ui.setupUi(room2)
    room2.show()
    sys.exit(app.exec_())

