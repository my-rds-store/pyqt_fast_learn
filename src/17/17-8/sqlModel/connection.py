#!/usr/bin/env python
#coding=utf-8


from PyQt4.QtCore import QString
from PyQt4.QtGui import QMessageBox
from PyQt4.QtSql import QSqlDatabase, QSqlQuery

def createConnection():

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("my.db")
    if (not db.open()):
        QMessageBox.critical(0, "Cannot open database1",
            "Unable to establish a database connection.", QMessageBox.Cancel)
        return False

    query =QSqlQuery()
    # 创建student表
    print query.exec_(QString("create table student (id int primary key, "
                                      "name varchar, course int)"))
    query.exec_(QString("insert into student values(1, '李强', 11)"))
    query.exec_(QString("insert into student values(2, '马亮', 11)"))
    query.exec_(QString("insert into student values(3, '孙红', 12)"))

    # 创建course表
    print query.exec_(QString("create table course (id int primary key, "
                                      "name varchar, teacher varchar)"))
    query.exec_(QString("insert into course values(10, '数学', '王老师')"))
    query.exec_(QString("insert into course values(11, '英语', '张老师')"))
    query.exec_(QString("insert into course values(12, '计算机', '白老师')"))
    return True


