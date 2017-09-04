#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtGui import QListWidgetItem, QPushButton,QApplication, \
    QIcon, QListWidget, QTreeWidget,QTreeWidgetItem, QTableWidget,QTableWidgetItem
from PyQt4.QtCore import Qt, QStringList
import sys


class My_button(QListWidgetItem, QPushButton):
    def __init__(self):
        QListWidgetItem.__init__()
        QPushButton.__init__("text")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # #********************* 1.  QListWidget ******************/
    listWidget = QListWidget()

    # 一种添加项目的简便方法
    QListWidgetItem("a", listWidget)

    # 添加项目的另一种方法，这样还可以进行各种设置
    listWidgetItem =  QListWidgetItem()
    listWidgetItem.setText("b")
    listWidgetItem.setIcon(QIcon("./yafeilinux.png"))
    listWidgetItem.setToolTip("this is b!")

    listWidget.insertItem(1, listWidgetItem)
    # 设置排序为倒序
    listWidget.sortItems(Qt.DescendingOrder)
    # 显示列表部件
    listWidget.show()

    #********************** 2. QTreeWidget *******************/

    treeWidget  = QTreeWidget()
    # 必须设置列数
    treeWidget.setColumnCount(2)
    # 设置标头
    headers = QStringList()
    headers.append("name")
    headers.append("year")

    treeWidget.setHeaderLabels(headers)
    # 添加项目
    grade1 =  QTreeWidgetItem(treeWidget)
    grade1.setText(0,"Grade1")
    student =  QTreeWidgetItem(grade1)
    student.setText(0,"Tom")
    student.setText(1,"1986")
    grade2 =  QTreeWidgetItem(treeWidget, grade1)
    grade2.setText(0,"Grade2")
    treeWidget.show()

    #********************* 3. QTableWidget ********************/
    # 创建表格部件，同时指定行数和列数
    tableWidget = QTableWidget(3, 2)
    # 创建表格项目，并插入到指定单元
    tableWidgetItem =  QTableWidgetItem("qt")
    tableWidget.setItem(1, 1, tableWidgetItem)
    # 创建表格项目，并将它们作为标头
    headerV =  QTableWidgetItem("first")
    tableWidget.setVerticalHeaderItem(0,headerV)
    headerH =  QTableWidgetItem("ID")
    tableWidget.setHorizontalHeaderItem(0,headerH)
    tableWidget.show()

    app.exec_()



