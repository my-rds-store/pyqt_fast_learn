#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtGui import QMainWindow,QTableView
from PyQt4.QtCore import Qt
from PyQt4.QtSql import QSqlQueryModel

class MainWindow(QMainWindow) :

    def __init__(self):
        super(MainWindow, self).__init__(None)

        self.model = QSqlQueryModel(self)
        self.model.setQuery("select * from student")
        self.model.setHeaderData(0, Qt.Horizontal, self.tr("学号"))
        self.model.setHeaderData(1, Qt.Horizontal, self.tr("姓名"))
        self.model.setHeaderData(2, Qt.Horizontal, self.tr("课程"))
        self.view = QTableView(self)
        self.view.setModel(self.model)
        self.setCentralWidget(self.view)

