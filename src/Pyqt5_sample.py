from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        xpos = 200
        ypos = 200
        width = 300
        height = 300
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("Taxi Management")
        self.iniUT()

    def iniUT(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome to the Taxi Management System")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()