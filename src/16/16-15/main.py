#!/usr/bin/env python
# encoding: utf-8

"""
@version : 
@author  : 
@license : 
@contact : ****@massclouds.com
@site    : http://blog.csdn.net/***
@software: PyCharm
@time    : 17-1-5 下午5:19
"""

from PyQt4.QtGui import QApplication, QListView
from PyQt4.QtCore import  QStringList, QVariant
import sys

from itemview import TtemView
from stringlistmodel import StringListModel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 1. 创建　模型 model  */
    qstrlist = QStringList()
    qstrlist.append("a")
    qstrlist.append("b")
    qstrlist.append("c")
    qstrlist.append("abcd")

    listV = QListView()
    stdItemModel = StringListModel(qstrlist,listV)
    listV.setModel(stdItemModel)
    listV.setWindowTitle("listV")
    listV.show()

    itemV = TtemView()
    itemV.setModel(stdItemModel)
    itemV.setWindowTitle("itemV")
    itemV.show()
    # 从第3行处,插入2行
    stdItemModel.insertRows(3, 2)

    # 获取3行０列  index
    index = stdItemModel.index(3, 0)
    stdItemModel.setData(index,QVariant("abc1234"))
    index = stdItemModel.index(4, 0)
    stdItemModel.setData(index,QVariant("tttt"))

    # 删除行
    stdItemModel.removeRows(0, 1)

    app.exec_()

