from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



def clicked():
    print("I am clicked!!!")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("First GUI Program")
    label = QtWidgets.QLabel(win)
    label.setText("Metro Dying Limited")
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click")
    b1.clicked.connect(clicked)
    label.move(50,50)
    win.show()
    sys.exit(app.exec_())
    
    
window()