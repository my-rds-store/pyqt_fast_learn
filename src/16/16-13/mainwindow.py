#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtCore import QString,  QStringList, QRegExp
from PyQt4.QtGui import  QMainWindow, QStringListModel,  QSortFilterProxyModel
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
        strlist = QStringList()
        strlist.append("yafei")
        strlist.append("yafeilinux")
        strlist.append("Qt")
        strlist.append("Qt Creator")

        listModel =  QStringListModel(strlist, self)
        self.filterModel =  QSortFilterProxyModel(self)
        # 为代理模型添加源模型
        self.filterModel.setSourceModel(listModel)
        # 在视图中使用代理模型
        self.listView.setModel(self.filterModel)

    def on_pushButton_clicked(self):
        rx = QRegExp(self.lineEdit.text())
        self.filterModel.setFilterRegExp(rx)

