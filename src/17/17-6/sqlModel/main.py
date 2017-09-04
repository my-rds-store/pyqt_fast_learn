#!/usr/bin/env python
#coding=utf-8

'''
FileName : main.py
'''

from PyQt4.QtCore import QTextCodec
from PyQt4.QtGui import QApplication
import sys

from connection import createConnection
from mainwindow import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    #  这两行代码要写在创建连接之前
    QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"))
    QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))
    if not createConnection():
        raise Exception("createConnection faild")
    win = MainWindow()
    win.show()
    app.exec_()
