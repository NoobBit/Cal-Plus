from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os, sys

class cal(QMainWindow):
    def __init__(self):
        super(cal, self).__init__()
        uic.loadUi("res/cal.ui", self)
        self.show()

        self.actions()

def main():
    app = QApplication([])
    window = cal()
    app.exec_()

if __name__ == "__main__":
    main()