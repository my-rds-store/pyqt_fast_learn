#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtGui import QMainWindow,QTableView
from PyQt4.QtSql import QSqlRelationalTableModel, QSqlRelation, \
                        QSqlRelationalDelegate
'''
FileName : mainwindow.py
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)

        model = QSqlRelationalTableModel(self)

        model.setTable("student")
        model.setRelation(2, QSqlRelation("course", "id", "name"))
        model.select()
        view = QTableView(self)
        view.setModel(model)
        self.setCentralWidget(view)

        view.setItemDelegate(QSqlRelationalDelegate(view))

