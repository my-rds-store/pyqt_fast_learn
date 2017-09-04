#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import QAbstractListModel, QStringList, QModelIndex, QVariant, Qt, QString


class StringListModel(QAbstractListModel):
    def __init__(self,stringList,parent = None):
        super(StringListModel, self).__init__(parent)
        self.stringList = QStringList(stringList)

    # int rowCount(const QModelIndex &parent = QModelIndex()) const;
    # QVariant data(const QModelIndex &index, int role) const;
    # QVariant headerData(int section, Qt::Orientation orientation,
    #                     int role = Qt::DisplayRole) const;

    def rowCount(self,parent=QModelIndex()):
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
