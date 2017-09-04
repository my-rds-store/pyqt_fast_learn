#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtCore import QString
from PyQt4.QtGui import  QMainWindow, QStandardItemModel, QStandardItem, \
    QDataWidgetMapper, QTableView
from PyQt4 import uic

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainWindow (QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi("mainwindow.ui", self)

        model =  QStandardItemModel(3, 2, self)
        model.setItem(0, 0, QStandardItem(_fromUtf8("xiaoming")))
        model.setItem(0, 1, QStandardItem(_fromUtf8("0")))
        model.setItem(1, 0, QStandardItem(_fromUtf8("xiaogang")))
        model.setItem(1, 1, QStandardItem(_fromUtf8("5")))
        model.setItem(2, 0, QStandardItem(_fromUtf8("xiaohong")))
        model.setItem(2, 1, QStandardItem(_fromUtf8("0")))
        model.setItem(3, 0, QStandardItem(_fromUtf8("赵六")))
        model.setItem(3, 1, QStandardItem(_fromUtf8("8")))

        self.mapper =  QDataWidgetMapper(self)
        # 设置模型
        self.mapper.setModel(model)
        # 设置窗口部件和模型中的列的映射
        self.mapper.addMapping(self.lineEdit, 0)
        self.mapper.addMapping(self.lineEdit_2, 1)
        # 显示模型中的第一行
        self.mapper.toFirst()

        #----------------------------------------------------------
        tableview  =  QTableView()
        tableview.setModel(model)
        tableview.show()

    # 上一条按钮
    def on_pushButton_clicked(self):
        self.mapper.toPrevious()

    # 下一条按钮
    def on_pushButton_2_clicked(self):
        self.mapper.toNext()

