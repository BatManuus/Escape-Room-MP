from re import A
from tkinter import DoubleVar
from tokenize import Double
from PyQt5 import QtCore, QtGui, QtWidgets,QtDesigner
from PyQt5.QtWidgets import QInputDialog,QPushButton,QWidget,QMessageBox
import time
import mysqlx
import mysql.connector as mc
#import MySQLdb.cursors as cursor


begin = time.time()

###DBMS
class Ui_room1(QWidget):

    
             
    
    def openWindow(self):
        from choice import Ui_choice
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_choice()
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
     
        self.door = QtWidgets.QPushButton(self.centralwidget)
        self.door.setGeometry(QtCore.QRect(0, 0, 80, 500))
        self.door.setText("")
        self.door.setStyleSheet("QPushButton{background: transparent;}")
        self.door.setObjectName("pushButton")
        self.door.clicked.connect(self.show_dialog)

        self.back = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.back.clicked.connect(room1.close)
        self.back.setGeometry(QtCore.QRect(20, 20, 91, 41))
        self.back.setIconSize(QtCore.QSize(150, 45))
        self.back.setStyleSheet("QPushButton{background : black; }")
        self.back.setObjectName("back")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(36, 28, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel {color : white; }")
        

        room1.setCentralWidget(self.centralwidget)

        self.retranslateUi(room1)
        QtCore.QMetaObject.connectSlotsByName(room1)
        

    def show_dialog(self, room1):
        
        exit = QInputDialog.getText(self, 'Exit ', "Enter The Code In Same Order:")
        user = ""
        room_name = ""
        time_1 = ""
        val =(user,time_1,room_name)
        if  exit == ('AXQS', True):
             user = QInputDialog.getText(self ,"UserID","Enter Your UserID")
             msg = QMessageBox()
             end = time.time()
             time_1 = (round((end - begin),2))
             room_name = "Room 1"
             msg.setWindowTitle("Congragulation")
             msg.setText("'"+str(user)+"' Completed The Room In '"+str(time_1)+"'")
             x = msg.exec_()
             print (user)
             self.openWindow()
             self.close()
             

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong")
            msg.setText("Try Again")
            x = msg.exec_()
            msg.setIcon(QMessageBox.Critical)
    
        myconn =mc.connect(host="localhost",user="root",password="chitta@12",database="demo_schema" )
        cursor = myconn.cursor()
        sql = "insert into high_score(username,time,room_name) values(%s,%s,%s)"
        val =(str(user),time_1,room_name)
        print(val)
        try:
             cursor.execute(sql,val)
             myconn.commit()
             print(cursor.rowcount,"record inserted")
        except:
             myconn.rollback()
             myconn.close()                    
             print(cursor.rowcount,"record not inserted")
    
    
             
    
        
      


    def show_dialog_1(self, room1):
        ok = QInputDialog.getText(self, 'Question Number 1', '1.What is data about data called?:')
        if  ok == ('metadata', True):
             msg = QMessageBox()
             msg.setWindowTitle("Congragulation")
             msg.setText("Your First Answer Alphabet is 'A' Note This Number")
             x = msg.exec_()
             msg.setIcon(QMessageBox.Critical)
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong")
            msg.setText("Try Again")
            x = msg.exec_()
            msg.setIcon(QMessageBox.Critical)

        
    def show_dialog_2(self, room1):
        ok = QInputDialog.getText(self, 'Question Number 2', '2.What level of data abstraction describes exactly how the data actually stored?')
        if  ok == ('physical', True):
             msg = QMessageBox()
             msg.setWindowTitle("Congragulation")
             msg.setText("Your Second Answer Alphabet is 'X' Note This Number")
             x = msg.exec_()
             msg.setIcon(QMessageBox.Critical)
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong")
            msg.setText("Try Again")
            x = msg.exec_()
            msg.setIcon(QMessageBox.Critical)
            


    def show_dialog_3(self, room1):
        ok = QInputDialog.getText(self, 'Question Number 3', '3.What refers to the number of tuples in a relation?')
        if  ok == ('cardinality', True):
             msg = QMessageBox()
             msg.setWindowTitle("Congragulation")
             msg.setText("Your Third Answer Alphabet is 'Q' Note This Number")
             x = msg.exec_()
             msg.setIcon(QMessageBox.Critical)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong")
            msg.setText("Try Again")
            x = msg.exec_()
            msg.setIcon(QMessageBox.Critical)


    def show_dialog_4(self, room1):
        ok = QInputDialog.getText(self, 'Question Number 4', '4.Which command is used to restore the database to the last committed state?')
        if  ok == ('Specialization', True):
             msg = QMessageBox()
             msg.setWindowTitle("Congragulation")
             msg.setText("Your Four Answer Alphabet is 'S' Note This Number")
             x = msg.exec_()
             msg.setIcon(QMessageBox.Critical)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong")
            msg.setText("Try Again")
            x = msg.exec_()
            msg.setIcon(QMessageBox.Critical)

    def retranslateUi(self, room1):
        _translate = QtCore.QCoreApplication.translate
        room1.setWindowTitle(_translate("room1", "Escape Room"))
        room1.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.label_3.setText(_translate("menu", "Forfeit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    room1 = QtWidgets.QMainWindow()
    ui = Ui_room1()
    ui.setupUi(room1)
    room1.show()
 
    sys.exit(app.exec_())


