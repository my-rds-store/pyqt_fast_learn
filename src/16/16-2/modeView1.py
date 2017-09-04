#!/usr/bin/env python
#coding=utf-8

#include <QApplication>
#include <QTreeView>
#include <QDebug>
#include <QStandardItemModel>
from PyQt4.QtCore import Qt, QModelIndex

from PyQt4.QtGui import QApplication, QStandardItemModel,QStandardItem, \
    QPixmap, QIcon, QTreeView, QColor
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    view = QTreeView()

    # 1.  模型
    '''
    PyQt使用Model时，如果Model创建时未设置parent，则运行完退出时会报错：
    QObject::startTimer: QTimer can only be used with threads started with QThread

    '''
    # model = QStandardItemModel()         # 创建标准项模型
    model = QStandardItemModel(view)         # 创建标准项模型
    # 获取模型的根项（Root Item），根项是不可见的
    parentItem = model.invisibleRootItem()

    # 创建标准项item0，并设置显示文本，图标和工具提示
    item0 = QStandardItem()
    item0.setText("A")
    pixmap0 = QPixmap(50,50)
    pixmap0.fill(QColor("red"))
    # pixmap0.fill(Qt.red)
    item0.setIcon(QIcon(pixmap0))
    item0.setToolTip("indexA")

    parentItem.appendRow(item0)  # 将item0  作为根项的子项

    # 将创建的标准项作为新的父项
    parentItem = item0
    # 创建新的标准项，它将作为item0的子项
    item1 = QStandardItem()
    item1.setText("B")
    pixmap1 = QPixmap(50,50)
    pixmap1.fill(Qt.blue)
    item1.setIcon(QIcon(pixmap1))
    item1.setToolTip("indexB")
    parentItem.appendRow(item1)

    # 创建新的标准项，这里使用了另一种方法来设置文本、图标和工具提示
    item2 = QStandardItem()
    pixmap2 = QPixmap(50,50)
    pixmap2.fill(Qt.green)
    item2.setData("C", Qt.EditRole)                  # 等同于  setText("C")
    item2.setData("indexC", Qt.ToolTipRole)          # 等同于  setToolTip("indexB")
    item2.setData(QIcon(pixmap2), Qt.DecorationRole) #等同于 setIcon(QIcon(pixmap1))
    parentItem.appendRow(item2)

    # 在树视图中显示模型
    view.setModel(model)
    view.show()

    # 获取item0的索引并输出item0的子项数目，然后输出了item1的显示文本和工具提示
    indexA = model.index(0, 0, QModelIndex())
    print  "indexA row count: " , model.rowCount(indexA)
    indexB = model.index(0, 0, indexA)
    print  "indexB text: " , model.data(indexB, Qt.EditRole).toString()
    print  "indexB toolTip: " , model.data(indexB, Qt.ToolTipRole).toString()

    app.exec_()




