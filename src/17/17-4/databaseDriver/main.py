#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtGui import QApplication
import sys

from PyQt4.QtSql import QSqlDatabase, QSqlQuery, QSqlDriver, QSqlRecord, QSqlField

from connection import createConnection

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # 创建数据库连接
    if not createConnection():
        raise Exception("createConnection faild")

    # # 使用QSqlQuery查询连接1的整张表，先要使用连接名获取该连接
    db1 = QSqlDatabase.database("connection1")
    query1 = QSqlQuery(db1)
    print "connection1:"
    query1.exec_("select * from student")
    while(query1.next()):
       print  query1.value(0).toInt(), " ", query1.value(1).toString()

    # 使用QSqlQuery查询连接2的整张表
    db2 = QSqlDatabase.database("connection2")
    query2 = QSqlQuery (db2)
    print "connection2:"
    query2.exec_("select * from student")
    while(query2.next()):
        print query2.value(0).toInt(), " ", query2.value(1).toString()

    # 以下是在例程17-4中添加的代码
    # 先判断该数据库驱动是否支持QuerySize特性，如果支持，则可以使用size()函数，
    # 如果不支持，那么就使用其他方法来获取总行数
    if (db2.driver().hasFeature(QSqlDriver.QuerySize)):
        print  "has feature: query size"
        numRows = query2.size()
    else:
        print   "no feature: query size"
        query2.last()
        numRows = query2.at() + 1

    print  "row number: %s " % numRows

    # 指向索引为1的记录，即第二条记录
    query2.seek(1)
    # 返回当前索引值
    print "current index:  %s " % query2.at()
    # 获取当前行的记录
    record = query2.record()
    # 获取记录中“id”和“name”两个属性的值
    id = record.value("id").toInt()
    name = record.value("name").toString()
    print   "id: %s name:  %s" %(id, name)
    # 获取索引为1的属性，即第二个属性
    field = record.field(1)
    # 输出属性名和属性值，结果为“name”和“MaLiang”
    print  "second field: %s field value: %s " % \
            (field.name(), field.value().toString())

    # app.exec_()

