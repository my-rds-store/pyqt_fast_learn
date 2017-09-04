#!/usr/bin/env python
#coding=utf-8

from PyQt4.QtGui import QItemDelegate, QSpinBox
from PyQt4.QtCore import Qt


class SpinBoxDelegate(QItemDelegate):
    def __init__(self,parent=None):
        super(SpinBoxDelegate, self).__init__(parent)


    # QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option,
    #                       const QModelIndex &index) const;
    #
    # void setEditorData(QWidget *editor, const QModelIndex &index) const;
    # void setModelData(QWidget *editor, QAbstractItemModel *model,
    #                   const QModelIndex &index) const;
    #
    # void updateEditorGeometry(QWidget *editor,const QStyleOptionViewItem &option,
    #                           const QModelIndex &index) const;


    # 创建编辑器 */
    def createEditor(self,parent, option, index ):

        editor =  QSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(100)

        return editor


    # 为编辑器设置数据 */
    def setEditorData(self,editor, index):

        value,flag = index.model().data(index, Qt.EditRole).toInt()
        spinBox =  editor
        spinBox.setValue(value)


    # 将数据写入到模型 */
    def setModelData(self, editor, model, index):

        spinBox =  editor
        spinBox.interpretText()
        value = spinBox.value()

        model.setData(index, value, Qt.EditRole)

    # 更新编辑器几何布局 */
    def updateEditorGeometry(self,editor, option, index ):

        editor.setGeometry(option.rect)

