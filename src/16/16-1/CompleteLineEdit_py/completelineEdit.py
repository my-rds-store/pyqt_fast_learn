#!/usr/bin/env python
# coding=utf-8

'''
FileName: main.py
'''

from PyQt4.QtGui import QLineEdit, QListView, QStringListModel, QFocusEvent
from PyQt4.QtCore import Qt, SIGNAL, SLOT, QStringList, QString, \
    QPoint, QModelIndex, pyqtSlot


class CompleteLineEdit(QLineEdit):
    def __init__(self, words):
        super(CompleteLineEdit, self).__init__(None)

        self.words = words                # QStringList  整个完成列表的单词
        self.listView = QListView(self)
        self.model = QStringListModel(self)
        self.listView.setWindowFlags(Qt.ToolTip)

        self.connect(self, SIGNAL("textChanged(const QString &)"),
                     self, SLOT("setCompleter(const QString &)"))

        self.connect(self.listView, SIGNAL("clicked(const QModelIndex &)"),
                     self, SLOT("completeText(const QModelIndex &)"))

    def focusOutEvent(self, focus_event):
        # self.listView.hide()
        pass

    @pyqtSlot("QKeyEvent")
    def keyPressEvent(self, e):
        if not self.listView.isHidden():
            key = e.key()
            count = self.listView.model().rowCount()
            currentIndex = self.listView.currentIndex()

            if Qt.Key_Down == key:
                # 按向下方向键时，移动光标选中下一个完成列表中的项
                row = currentIndex.row() + 1
                if (row >= count):
                    row = 0

                index = self.listView.model().index(row, 0)
                self.listView.setCurrentIndex(index)
            elif Qt.Key_Up == key:
                # 按向下方向键时，移动光标选中上一个完成列表中的项
                row = currentIndex.row() - 1
                if (row < 0):
                    row = count - 1

                index = self.listView.model().index(row, 0)
                self.listView.setCurrentIndex(index)
            elif Qt.Key_Escape == key:
                # 按下Esc键时，隐藏完成列表
                self.listView.hide()
            elif Qt.Key_Enter == key or Qt.Key_Return == key:
                # 按下回车键时，使用完成列表中选中的项，并隐藏完成列表
                if (currentIndex.isValid()):
                    text = self.listView.currentIndex().data().toString()
                    self.setText(text)

                self.listView.hide()
            else:
                # 其他情况，隐藏完成列表，并使用QLineEdit的键盘按下事件
                self.listView.hide()
                QLineEdit.keyPressEvent(self,e)
        else:
            QLineEdit.keyPressEvent(self,e)

    # 动态的显示完成列表
    @pyqtSlot("QString")
    def setCompleter(self, text):

        if (text.isEmpty()):
            self.listView.hide()
            return

        if text.length() > 1 and not self.listView.isHidden():
            return

        # 如果完整的完成列表中的某个单词包含输入的文本，则加入要显示的完成列表串中
        sl = QStringList()

        for i in range(self.words.count()):
            if self.words[i].contains(text):
                sl << self.words[i]

        self.model.setStringList(sl)
        self.listView.setModel(self.model)

        if (self.model.rowCount() == 0):
            return

        # Position the text edit
        self.listView.setMinimumWidth(self.width())
        self.listView.setMaximumWidth(self.width())

        p = QPoint(0, self.height())
        x = self.mapToGlobal(p).x()
        y = self.mapToGlobal(p).y() + 1

        self.listView.move(x, y)
        self.listView.show()

    # 点击完成列表中的项，使用此项自动完成输入的单词
    @pyqtSlot("QModelIndex")
    def completeText(self, index):
        text = index.data().toString()
        self.setText(text)
        self.listView.hide()
