#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import QString, QModelIndex, SIGNAL
from PyQt4.QtGui import QTableView, QMainWindow, \
    QStandardItemModel, QStandardItem, QItemSelection, \
    QItemSelectionModel
from PyQt4 import uic

from spinboxdelegate import SpinBoxDelegate

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

        self.connect(selectionModel,SIGNAL("selectionChanged(QItemSelection,QItemSelection)"),
                     self.updateSelection)
        self.connect(selectionModel, SIGNAL("currentChanged(QModelIndex,QModelIndex)"),
                self.changeCurrent)

        # 多个视图共享选择
        self.tableView2 = QTableView()
        self.tableView2.setWindowTitle("tableView2")
        self.tableView2.resize(400, 300)
        self.tableView2.setModel(model)
        self.tableView2.setSelectionModel(selectionModel)
        self.tableView2.show()

        # 使用自定义委托
        delegate = SpinBoxDelegate(self)
        self.tableView.setItemDelegate(delegate)

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

    # 更新选择
    def updateSelection(self,selected, deselected):

        mlist = selected.indexes()
        # 为现在选择的项目填充值
        for index in mlist:
            text = QString("(%1,%2)").arg(index.row()).arg(index.column())
            self.tableView.model().setData(index, text)

        mlist = deselected.indexes()
        # 清空上一次选择的项目的内容
        for index in mlist:
            self.tableView.model().setData(index, "")

    # 改变当前项目
    def changeCurrent(self, current, previous):

        print  QString("move(%1,%2) to (%3,%4)")\
            .arg(previous.row()).arg(previous.column()) \
            .arg(current.row()).arg(current.column())
