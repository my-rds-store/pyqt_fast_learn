#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtCore import QString, QModelIndex
from PyQt4.QtGui import QTableView, QMainWindow,  \
    QStandardItemModel, QStandardItem, QItemSelection, \
    QItemSelectionModel
from PyQt4 import uic

class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super(MainWindow, self).__init__(None)
        uic.loadUi("mainwindow.ui",self)


        model = QStandardItemModel(7, 4, self)
        for row in range(7):
            for column in range(4):
                item = QStandardItem(QString("%1").arg(row * 4 + column))
                model.setItem(row, column, item)

        tableView =  QTableView()
        tableView.setModel(model)
        self.setCentralWidget(tableView)

        #获取视图的项目选择模型
        selectionModel = tableView.selectionModel()
        # 定义左上角和右下角的索引，然后使用这两个索引创建选择
        topLeft = model.index(1, 1, QModelIndex())
        bottomRight = model.index(5, 2, QModelIndex())
        selection = QItemSelection(topLeft, bottomRight)
        # 使用指定的选择模式来选择项目
        selectionModel.select(selection, QItemSelectionModel.Select)

