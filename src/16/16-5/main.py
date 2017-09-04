#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import QStringList

from PyQt4.QtGui import QApplication, QListView, QTableView
import sys
from stringlistmodel import StringListModel

if __name__ == "__main__":

    app = QApplication(sys.argv)

    qlist = QStringList()
    qlist.append("a")
    qlist.append("b")
    qlist.append("c")


    listView = QListView()
    tableView = QTableView()
    '''

    PyQt使用Model时，如果Model创建时未设置parent，则运行完退出时会报错：

    QObject::startTimer: QTimer can only be used with threads started with QThread

    '''
    # model = StringListModel(qlist)
    model = StringListModel(qlist,listView)

    listView.setModel(model)
    listView.show()

    tableView.setModel(model)
    tableView.show()

    # 插入删除行
    model.insertRows(3, 2)
    model.removeRows(0, 1)

    app.exec_()

