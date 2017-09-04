#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtCore import QString, QModelIndex
from PyQt4.QtGui import QTableView, QMainWindow, \
    QStandardItemModel, QStandardItem, QItemSelection, \
    QItemSelectionModel
from PyQt4 import uic

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("mainwindow.ui", self)

        model = QStandardItemModel(7, 4, self)
        for row in range(7):
            for column in range(4):
                item = QStandardItem(QString("%1").arg(row * 4 + column))
                model.setItem(row, column, item)

        self.tableView = QTableView()
        self.tableView.setModel(model)
        self.setCentralWidget(self.tableView)

        # 获取视图的项目选择模型
        selectionModel = self.tableView.selectionModel()

        # 定义左上角和右下角的索引，然后使用这两个索引创建选择
        topLeft = model.index(1, 1, QModelIndex())
        bottomRight = model.index(5, 2, QModelIndex())
        selection = QItemSelection(topLeft, bottomRight)

        # 使用指定的选择模式来选择项目
        selectionModel.select(selection, QItemSelectionModel.Select)

        self.mainToolBar.addAction(_fromUtf8("当前项目"), self.getCurrentItemData)
        self.mainToolBar.addAction(_fromUtf8("切换选择"), self.toggleSelection)

    # 输出当前项目的内容
    def getCurrentItemData(self, ):

        print  "当前项目的内容：", \
            self.tableView.selectionModel().currentIndex().data().toString()

    # 切换选择的项目
    def toggleSelection(self):
        topLeft = self.tableView.model().index(0, 0, QModelIndex())
        bottomRight = self.tableView.model().index(
            self.tableView.model().rowCount(QModelIndex()) - 1,
            self.tableView.model().columnCount(QModelIndex()) - 1, QModelIndex())
        curSelection = QItemSelection(topLeft, bottomRight)
        self.tableView.selectionModel().select(curSelection, QItemSelectionModel.Toggle)
