#!/usr/bin/env python
#coding=utf-8

'''
FileName: main.py
'''

import sys
from PyQt4.QtCore import QString, SIGNAL,QStringList,Qt
from PyQt4.QtGui import QApplication, QLineEdit ,QCompleter,\
        QDirModel, QStringListModel

# QCompleter补全文件路径
class FilePath(QLineEdit):

    def __init__(self):
        super(FilePath, self).__init__(None)

        self.setWindowTitle("FilePath")
        completer = QCompleter(self)
        dir_model = QDirModel()
        dir_model.setParent(self)
        completer.setModel(dir_model)
        self.setCompleter(completer)

# QCompleter补全单词
class  CWord(QLineEdit):

    def __init__(self):
        super(CWord, self).__init__(None)

        self.setWindowTitle("CWord")

        word_list = QStringList()
        word_list<<"Java"<<"C++"<<"C#"<<"PHP"<<"Perl"<<"Python"<<"Delphi"<<"Ruby"
        completer2 = QCompleter(word_list, self)
        completer2.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompleter(completer2)

# QCompleter添加新单词
class AddNewWord(QLineEdit):

    def __init__(self):
        super(AddNewWord, self).__init__(None)

        self.setWindowTitle("AddNewWord")

        completer = QCompleter(self)
        self.string_list_model = QStringListModel(self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setModel(self.string_list_model)
        self.setCompleter(completer)
        self.connect(self, SIGNAL("editingFinished()"), self.editComplete)

        self.word_list = QStringList()

    def editComplete(self):
        text = self.text()
        if QString.compare(text, QString("")) != 0:

            is_contains = self.word_list.contains(text, Qt.CaseInsensitive)
            if not is_contains:
                self.word_list<<text
                self.string_list_model.setStringList(self.word_list)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # QCompleter补全文件路径
    win_fpath = FilePath()
    win_fpath.show()

    # QCompleter补全单词
    cword = CWord()
    cword.show()

    # QCompleter添加新单词
    add_world = AddNewWord()
    add_world.show()

    app.exec_()

