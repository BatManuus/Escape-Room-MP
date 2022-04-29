from PyQt5 import QtCore, QtGui, QtWidgets
from choice import Ui_choice
from corridor import Ui_corridor



class Ui_menu(QtWidgets.QMainWindow):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_choice()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_corridor()
        self.ui.setupUi(self.window)
        self.window.show()


    def openWindow2(self):
        from main import Ui_Main
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()        



    def setupUi(self, menu):
        menu.setObjectName("Escape Room")
        menu.resize(801, 601)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        menu.setFont(font)
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        
        self.bg2 = QtWidgets.QLabel(self.centralwidget)
        self.bg2.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.bg2.setText("")
        self.bg2.setPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/menu1.png"))
        self.bg2.setObjectName("bg2")
        
        self.soloR = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow())
        self.soloR.clicked.connect(menu.close)
        self.soloR.setGeometry(QtCore.QRect(80, 200, 241, 251))
        self.soloR.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/Solo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soloR.setIcon(icon)
        self.soloR.setIconSize(QtCore.QSize(250, 250))
        self.soloR.setObjectName("soloR")
        
        self.multiR = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow1())
        self.multiR.clicked.connect(menu.close)
        self.multiR.setGeometry(QtCore.QRect(430, 200, 241, 251))
        self.multiR.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/multi_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.multiR.setIcon(icon1)
        self.multiR.setIconSize(QtCore.QSize(250, 250))
        self.multiR.setObjectName("multiR")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 426, 91, 21))
        self.label.setStyleSheet("QLabel { background-color : none; color : white; }")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(504, 426, 121, 21))
        self.label_2.setStyleSheet("QLabel { background-color : none; color : white; }")
        self.label_2.setObjectName("label_2")
        
        self.back = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.openWindow2())
        self.back.clicked.connect(menu.close)
        self.back.setGeometry(QtCore.QRect(20, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.back.setFont(font)
        self.back.setAutoFillBackground(False)
        self.back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon2)
        self.back.setIconSize(QtCore.QSize(150, 45))
        self.back.setObjectName("back")
       
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(46, 28, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("QLabel {color : white; }")
        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Escape Room"))
        menu.setWindowIcon(QtGui.QIcon("C:/Users/gorug/PycharmProjects/EscapeRoom-MP/images/logo1.png"))
        self.label.setText(_translate("menu", "Solo Rooms"))
        self.label_2.setText(_translate("menu", "Multiple Rooms"))
        self.label_3.setText(_translate("menu", "Back"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QMainWindow()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
