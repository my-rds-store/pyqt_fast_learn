#!/usr/bin/env python
# encoding: utf-8

"""
@version : 
@author  : 
@license : 
@contact : ****@massclouds.com
@site    : http://blog.csdn.net/***
@software: PyCharm
@time    : 17-1-5 下午5:19
"""

from PyQt4.QtGui import QApplication,QTreeView,QFileSystemModel, QListView
from PyQt4.QtCore import QDir
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 1. 创建　模型 model  */
    model = QFileSystemModel()            # 创建文件系统模型
    model.setRootPath(QDir.currentPath()) # 指定要监视的目录

    # 2. 创建　视图 view  */
    tree = QTreeView()                                 # 创建树型视图
    tree.setModel(model)                               # 为视图指定模型
    tree.setRootIndex(model.index(QDir.currentPath() ))# 指定根索引

    listw = QListView()                                # 创建列表视图
    listw.setModel(model)                              # 为视图指定模型
    listw.setRootIndex(model.index(QDir.currentPath()))# 指定根索引

    tree.setWindowTitle("QTreeView")
    tree.show()
    listw.setWindowTitle("QListView")
    listw.show()

    app.exec_()
