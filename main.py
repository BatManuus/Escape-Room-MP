from PyQt5 import QtCore, QtGui, QtWidgets
from highscore import Ui_highscore
from menu import Ui_menu

class Ui_Main(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_highscore()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(801, 601)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        Main.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        
        self.bg1 = QtWidgets.QLabel(self.centralwidget)
        self.bg1.setGeometry(QtCore.QRect(0, 0, 801, 601))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.bg1.setFont(font)
        self.bg1.setText("")
        self.bg1.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/Escape-Room.png"))
        self.bg1.setObjectName("bg1")
        #####

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        
        self.start1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.start1.clicked.connect(Main.close)
        self.start1.setGeometry(QtCore.QRect(630, 370, 150, 45))
        self.start1.setFont(font)
        self.start1.setAutoFillBackground(False)
        self.start1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.start1.setIcon(icon)
        self.start1.setIconSize(QtCore.QSize(150, 45))
        self.start1.setObjectName("start1")
        
        
        self.option1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow1())
        self.start1.clicked.connect(Main.close)
        self.option1.setGeometry(QtCore.QRect(630, 430, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        self.option1.setFont(font)
        self.option1.setText("")
        self.option1.setIcon(icon)
        self.option1.setIconSize(QtCore.QSize(150, 45))
        self.option1.setObjectName("option1")
        
        self.exit1 = QtWidgets.QPushButton(self.centralwidget)
        self.exit1.clicked.connect(Main.close)
        self.exit1.setGeometry(QtCore.QRect(630, 490, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.exit1.setFont(font)
        self.exit1.setText("")
        self.exit1.setIcon(icon)
        self.exit1.setIconSize(QtCore.QSize(150, 45))
        self.exit1.setObjectName("exit1")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(683, 385, 87, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel {color : white; }")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 442, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel {color : white; }")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(683, 505 , 87, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel {color : white; }")
        
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Escape Room"))
        Main.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.label.setText(_translate("Main", "Start"))
        self.label_2.setText(_translate("Main", "HighScore"))
        self.label_3.setText(_translate("Main", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
