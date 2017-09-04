#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtCore import QString,Qt,pyqtSlot
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
from PyQt4.QtSql import  QSqlTableModel
from PyQt4 import uic


class MainWindow(QMainWindow) :
    def __init__(self):
        super(MainWindow, self).__init__(None)
        uic.loadUi("mainwindow.ui",self)

        self.model =  QSqlTableModel(self)
        self.model.setTable("student")
        self.model.select()
        # 设置编辑策略
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tableView.setModel(self.model)


    # 提交修改按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 开始事务操作
        self.model.database().transaction() # 启动 事物操作
        if (self.model.submitAll()):
            self.model.database().commit() #提交
        else:
            self.model.database().rollback() #回滚
            QMessageBox.warning(self, self.tr("tableModel"),
                                 self.tr("数据库错误: %1").arg(self.model.lastError().text()))

    # 撤销修改按钮
    @pyqtSlot()
    def on_pushButton_2_clicked(self):

        self.model.revertAll()

    # 查询按钮，进行筛选
    @pyqtSlot()
    def on_pushButton_7_clicked(self):

        name = self.lineEdit.text()
        #根据姓名进行筛选，一定要使用单引号
        #model.setFilter(QString("name = '%1'").arg(name)) # filter 过滤器
        self.model.setFilter(QString("name LIKE '%%%1%%'").arg(name)) # filter过滤器,模糊查询
        self.model.select()

    # 显示全表按钮
    @pyqtSlot()
    def on_pushButton_8_clicked(self):

        self.model.setTable("student")
        self.model.select()

    # 按id升序排列按钮
    @pyqtSlot()
    def on_pushButton_5_clicked(self):

        #id属性，即第0列，升序排列
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()

    # 按id降序排列按钮
    @pyqtSlot()
    def on_pushButton_6_clicked(self):

        self.model.setSort(0, Qt.DescendingOrder)
        self.model.select()

    # 删除选中行按钮
    @pyqtSlot()
    def on_pushButton_4_clicked(self):

        # 获取选中的行
        curRow = self.tableView.currentIndex().row()
        # 删除该行
        self.model.removeRow(curRow)
        ok = QMessageBox.warning(self,self.tr("删除当前行!"),
                      self.tr("你确定删除当前行吗？"),QMessageBox.Yes, QMessageBox.No)
        if(ok == QMessageBox.No):
         # 如果不删除，则撤销
            self.model.revertAll()
        else:  # 否则提交，在数据库中删除该行
            self.model.submitAll()

    # 添加记录按钮
    @pyqtSlot()
    def on_pushButton_3_clicked(self):

        # 获得表的行数
        rowNum = self.model.rowCount()
        id = 10
        # 添加一行
        self.model.insertRow(rowNum)
        self.model.setData(self.model.index(rowNum,0), id)
        # 可以直接提交
        #model.submitAll()

