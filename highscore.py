from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysqlx
import mysql.connector as mc
import MySQLdb.cursors as cursor
import ast
from sqlalchemy import column



def MyConverter(mydata):
    def cvt(high_score):
        try:
            return ast.literal_eval(high_score)

        except Exception:
            return str(high_score)
    return tuple(map(cvt,mydata))




class Ui_highscore(object):
    def openWindow(self):
        from main import Ui_Main
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()


    def LoadData(self):
        myconn =mc.connect(host="localhost",user="root", password="chitta@12",database="demo_schema",)
        with myconn:
            cursor = myconn.cursor()
            row = cursor.execute("SELECT * from high_score")
            high_score = cursor.fetchall()

            for row in high_score:
                self.addTable(MyConverter(row))
            cursor.close()

            
    def addTable(self,columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i,column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i ,QtWidgets.QTableWidgetItem(str(column)))
                


    def setupUi(self, highscore):
        highscore.setObjectName("highscore")
        highscore.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(highscore)
        self.centralwidget.setObjectName("centralwidget")
        
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../images/login_1.png"))
        self.bg.setObjectName("bg")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 90, 551, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setItem(0,0, QTableWidgetItem("UserName"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Time"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Room Name"))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        highscore.setFont(font)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)

        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.clicked.connect(self.LoadData)
        self.refresh.setGeometry(QtCore.QRect(20, 20, 91, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh.setIcon(icon2)
        self.refresh.setIconSize(QtCore.QSize(150, 45))
        self.refresh.setObjectName("refresh")

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.clicked.connect(self.openWindow)
        self.back.setGeometry(QtCore.QRect(20, 80, 91, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon2)
        self.back.setIconSize(QtCore.QSize(150, 45))
        self.back.setObjectName("back")
       
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        highscore.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel {color : white; }")
        highscore.setCentralWidget(self.centralwidget)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(46, 88, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        highscore.setFont(font)
        self.label_2.setObjectName("label_3")
        self.label_2.setStyleSheet("QLabel {color : white; }")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 28, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        highscore.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel {color : white; }")

        self.retranslateUi(highscore)
        QtCore.QMetaObject.connectSlotsByName(highscore)

    def retranslateUi(self, highscore):
        _translate = QtCore.QCoreApplication.translate
        highscore.setWindowTitle(_translate("highscore", "MainWindow"))
        self.label.setText(_translate("highscore", "Scores"))
        self.label_2.setText(_translate("menu", "Back"))
        self.label_3.setText(_translate("menu", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    highscore = QtWidgets.QMainWindow()
    ui = Ui_highscore()
    ui.setupUi(highscore)
    highscore.show()
    sys.exit(app.exec_())
