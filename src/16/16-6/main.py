#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtGui import QApplication
import sys
from mainwindow import MainWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()

