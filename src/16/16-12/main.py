#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtGui import  QApplication, QAbstractItemView, QListView,QTableView
from PyQt4.QtCore import  QStringList
import sys
from stringlistmodel import StringListModel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    slist = QStringList()
    slist.append("a")
    slist.append("b")
    slist.append("c")
    slist.append("d")

    listView = QListView()
    '''
    PyQt使用Model时，如果Model创建时未设置parent，则运行完退出时会报错：
    QObject::startTimer: QTimer can only be used with threads started with QThread
    '''
    # model = StringListModel(slist)
    model = StringListModel(slist,listView)

    listView.setModel(model)
    listView.show()

    tableView = QTableView ()
    tableView.setModel(model)
    tableView.show()

    # 插入删除行
    model.insertRows(3, 2)
    model.removeRows(0, 1)

    # 启用拖放功能
    listView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置拖放为移动，　默认为复制
    listView.setDragEnabled(True)  # 启用拖动
    listView.setAcceptDrops(True)  # 设置接受拖放
    listView.setDropIndicatorShown(True) # 设置显示将要被放置的位置

    app.exec_()
