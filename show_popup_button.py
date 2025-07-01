

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainButton.setGeometry(QtCore.QRect(250, 180, 311, 161))
        self.mainButton.setObjectName("mainButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.mainButton.clicked.connect(self.show_popup)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainButton.setText(_translate("MainWindow", "Show Popup"))


    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Hello I am Popup")
        msg.setText("Hello Tanvir, How are you??")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry | QMessageBox.Ignore )
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("This is very informative message for you")
        msg.setDetailedText("This is my very details text message...")
        msg.buttonClicked.connect(self.debug)
        x = msg.exec_()


    def debug(self,i):
        print(i.text())
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





# QMessageBox.Question
# QMessageBox.Ok
# QMessageBox.Cancel
# QMessageBox.Save
# QMessageBox.Close
# QMessageBox.Yes
# QMessageBox.No
# QMessageBox.Abort
# QMessageBox.Ignore
# QMessageBox.Retry

