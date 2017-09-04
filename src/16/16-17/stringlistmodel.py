#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import QAbstractListModel, QStringList, QModelIndex, QVariant, Qt, QString, QAbstractItemModel, SIGNAL


class StringListModel(QAbstractListModel):
    def __init__(self,stringList,parent = None):
        super(StringListModel, self).__init__(parent)
        self.stringList = QStringList(stringList)

    # int rowCount(const QModelIndex &parent = QModelIndex()) const;
    # QVariant data(const QModelIndex &index, int role) const;
    # QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;
    # // 编辑功能用到的两个函数
    # Qt::ItemFlags flags(const QModelIndex &index) const;
    # bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole);
    #
    # // 插入和删除行用到的两个函数
    # bool insertRows(int position, int rows, const QModelIndex &index = QModelIndex());
    # bool removeRows(int position, int rows, const QModelIndex &index = QModelIndex());

    def rowCount(self,parent= QModelIndex()):
        return self.stringList.count()

    def data(self,index,role= Qt.DisplayRole):

        if (not index.isValid()):
            return QVariant()

        if (index.row() >= self.stringList.count):
            return QVariant()

        if (role == Qt.DisplayRole):
            return self.stringList[index.row()]
        else:
            return QVariant()
    def headerData(self,section, orientation, role= Qt.DisplayRole):

        if (role != Qt.DisplayRole):
            return QVariant()

        if (orientation == Qt.Horizontal):
            return QString("Column %1").arg(section)
        else:
            return QString("Row %1").arg(section)

    # 以下是实现编辑功能添加的两个函数

    def flags(self,index):
        if (not index.isValid()):
            return Qt.ItemIsEnabled

        return super(StringListModel, self).flags(index) | Qt.ItemIsEditable

    def setData(self, index, value, role= Qt.EditRole):

        if (index.isValid() and role == Qt.EditRole):
            self.stringList.replace(index.row(), value.toString())
            self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"),index, index)
            return  True
        return False

    # 以下是插入和删除行用到的两个函数
    def insertRows(self,position, rows, parent = QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position+rows-1)

        for i in range(rows):
            self.stringList.insert(position, "")

        self.endInsertRows()
        return True

    def removeRows(self,position, rows, parent = QModelIndex()):

        self.beginRemoveRows(QModelIndex(), position, position+rows-1)

        for i in range(rows):
            self.stringList.removeAt(position)

        self.endRemoveRows()
        return True

