#!/usr/bin/env python
#coding=utf-8

'''
FileName: main.py
'''

import sys
from PyQt4.QtCore import QStringList
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QHBoxLayout

from completelineEdit import CompleteLineEdit

if __name__ == "__main__":

    app = QApplication(sys.argv)

    sl = QStringList() << "Biao" << "Bin" << "Huang" << "Hua" << "Hello" << "BinBin" << "Hallo"
    widgetw = QWidget()
    edit= CompleteLineEdit(sl)
    button = QPushButton("Button")
    layout = QHBoxLayout()
    layout.addWidget(edit)
    layout.addWidget(button)
    widgetw.setLayout(layout)

    widgetw.show()

    # e = CompleteLineEdit(sl)
    # e.show()

    app.exec_()

