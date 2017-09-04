#!/usr/bin/env python
#coding=utf-8

#include <QApplication>

#include <QListView>
#include <QTableView>
#include <QDebug>
import sys
from PyQt4.QtCore import QStringList
from PyQt4.QtGui import QApplication, QListView, QTableView
from stringlistmodel import StringListModel

if __name__ == "__main__":

    app = QApplication(sys.argv)

    qlist = QStringList()
    qlist.append("a")
    qlist.append("b")
    qlist.append("c")
    qlist.append("abcd")

    model = StringListModel(qlist)

    qlistView = QListView()
    qlistView.setModel(model)
    qlistView.show()

    tableView = QTableView()
    tableView.setModel(model)
    tableView.show()

    app.exec_()
