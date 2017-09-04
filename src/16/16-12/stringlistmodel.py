#!/usr/bin/env python
# coding=utf-8

from PyQt4.QtCore import QAbstractListModel, QStringList, Qt, QVariant, \
    QString, SIGNAL, QModelIndex, QMimeData, QByteArray, QIODevice, QDataStream


class StringListModel(QAbstractListModel):
    def __init__(self, strings, parent=None):
        super(StringListModel, self).__init__(parent)
        self.stringList = strings

    #
    # int rowCount( QModelIndex &parent = QModelIndex()):
    # QVariant data( QModelIndex &index, int role):
    # QVariant headerData(int section, Qt.Orientation orientation,
    #                     int role = Qt.DisplayRole):
    # # 编辑功能用到的两个函数
    # Qt.ItemFlags flags( QModelIndex &index):
    # bool setData( QModelIndex &index,  QVariant &value,
    #              int role = Qt.EditRole)
    #
    # # 插入和删除行用到的两个函数
    # bool insertRows(int position, int rows,  QModelIndex &index = QModelIndex())
    # bool removeRows(int position, int rows,  QModelIndex &index = QModelIndex())
    #
    # # 以下函数在例程16-12中添加，用来实现拖放功能
    # Qt.DropActions supportedDropActions():
    # QStringList mimeTypes():
    # QMimeData *mimeData( QModelIndexList &indexes):
    # bool dropMimeData( QMimeData *data, Qt.DropAction action,
    #                                          int row, int column,  QModelIndex &parent)

    def rowCount(self, parent):

        return self.stringList.count()

    def data(self, index, role=Qt.DisplayRole):

        if (not index.isValid()):
            return QVariant()

        if (index.row() >= self.stringList.count):
            return QVariant()

        # 添加Qt.EditRole的判断
        if (role == Qt.DisplayRole or role == Qt.EditRole):
            value  = self.stringList[index.row()]
            return QVariant(value)
        else:
            return QVariant()

    def headerData(self, section, orientation, role):

        if (role != Qt.DisplayRole):
            return QVariant()

        if (orientation == Qt.Horizontal):
            return QString("Column %1").arg(section)
        else:
            return QString("Row %1").arg(section)

    # 以下是实现编辑功能添加的两个函数

    # 在例程16-12中进行了修改，来支持拖放操作
    def flags(self, index):

        # 如果该索引无效，那么只支持放入操作
        if (not index.isValid()):
            return Qt.ItemIsEnabled | Qt.ItemIsDropEnabled

        # 如果该索引有效，那么既支持拖拽操作，也支持放入操作
        return super(StringListModel, self).flags(index) | Qt.ItemIsEditable \
               | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

    def setData(self, index, value, role=Qt.EditRole):

        if (index.isValid() and role == Qt.EditRole):
            self.stringList.replace(index.row(), value.toString())
            self.emit(SIGNAL("dataChanged(QModelIndex, QModelIndex)"), index, index)
            return True

        return False

    # 以下是插入和删除行用到的两个函数
    def insertRows(self, position, rows, parent = QModelIndex()):

        self.beginInsertRows(QModelIndex(), position, position + rows - 1)

        # for (int row = 0 row < rows ++row)
        for row in range(rows):
            self.stringList.insert(position, "")

        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent  = QModelIndex()):

        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

        # for (int row = 0 row < rows ++row)
        for row in range(rows):
            self.stringList.removeAt(position)

        self.endRemoveRows()
        return True

    # 以下函数在例程16-12中添加，用来实现拖放功能
    # 设置支持放入动作
    def supportedDropActions(self):

        # return Qt.CopyAction | Qt.MoveAction   # 复制
        return  Qt.MoveAction    # 移动

    # 设置在拖放操作中导出的条目的数据的编码类型
    def mimeTypes(self):

        types = QStringList()
        # "application/vnd.text.list"是自定义的类型，在后面的函数中要保持一致
        types << "application/vnd.text.list"
        # types.append("application/vnd.text.list")
        return types

    # 将拖放的数据放入QMimeData中
    def mimeData(self, indexes):

        _mimeData = QMimeData()
        encodedData = QByteArray()

        stream = QDataStream(encodedData, QIODevice.WriteOnly)
        for index in indexes:
            if (index.isValid()):
                text = self.data(index, Qt.DisplayRole).toString()
                stream << text

        # 将数据放入QMimeData中
        _mimeData.setData("application/vnd.text.list", encodedData)
        return _mimeData

    # 将拖放的数据放入模型中
    def dropMimeData(self, data, action, row, column, parent):

        # 如果放入动作是Qt.IgnoreAction，那么返回True
        if (action == Qt.IgnoreAction):
            return True
        # 如果数据的格式不是指定的格式，那么返回False
        if (not data.hasFormat("application/vnd.text.list")):
            return False
        # 因为这里是列表，只用一列，所以列大于0时返回False
        if (column > 0):
            return False
        # 设置开始插入的行
        if (row != -1):
            beginRow = row
        elif parent.isValid():
            beginRow = parent.row()
        else:
            beginRow = self.rowCount(QModelIndex())

        # 将数据从QMimeData中读取出来，然后插入到模型中
        encodedData = data.data("application/vnd.text.list")
        stream = QDataStream(encodedData, QIODevice.ReadOnly)

        newItems = QStringList()
        rows = 0

        while (not stream.atEnd()):
            text = QString()
            stream >> text
            newItems.append(text)
            rows += 1

        self.insertRows(beginRow, rows, QModelIndex())
        for text in newItems:
            idx = self.index(beginRow, 0, QModelIndex())
            self.setData(idx,QVariant(text) )
            beginRow += 1

        return True
