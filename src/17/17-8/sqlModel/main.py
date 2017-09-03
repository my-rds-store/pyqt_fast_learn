#!/usr/bin/env python
#coding=utf-8


'''
 sudo apt-get install python-qt4-sql
'''

import sys
from connection import createConnection

from PyQt4.QtCore import QTextCodec
from PyQt4.QtGui import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":


    app = QApplication (sys.argv)
    # 这行代码要写在创建连接之前
    QTextCodec.setCodecForTr(QTextCodec.codecForName("UTF-8"))
    QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))

    if not createConnection():
        raise Exception("createConnection faild")
    w = MainWindow()
    w.show()
    app.exec_()
