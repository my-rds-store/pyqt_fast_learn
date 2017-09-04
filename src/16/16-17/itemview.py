#!/usr/bin/env python
# encoding: utf-8

"""
@version :
@author  :
@license :
@contact : ****@massclouds.com
@site    : http://blog.csdn.net#**
@software: PyCharm
@time    : 17-1-5 下午5:19
"""
from PyQt4.QtCore import QModelIndex, QRect, SIGNAL
from PyQt4.QtGui import QAbstractItemView, QRegion,QGridLayout, \
    QLabel,QPushButton,QWidget


class TtemView(QAbstractItemView):
    def __init__(self, parent=None):
        super(TtemView, self).__init__(parent)
        self.gridLayout = QGridLayout(self)

        # # print "*"  * 100
        # self.listw[:] = []
        # print self.listw.__len__()

    # public:
    #     QRect visualRect(const QModelIndex &index) const
    #     QModelIndex indexAt(const QPoint &point) const
    #
    # protected slots:
    #     void dataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight)
    #     void rowsInserted(const QModelIndex &parent, int start, int end)
    #     void rowsAboutToBeRemoved(const QModelIndex &parent, int start, int end)


    def dataChanged(self, topLeft, bottomRight):
        super(TtemView, self).dataChanged(topLeft, bottomRight)

        print "topLeft : " ,topLeft.column(),",", topLeft.row()
        print "bottomRight : " ,bottomRight.column(),",", bottomRight.row()
        print "rowCount:" ,self.model().rowCount(self.rootIndex())
        print "data:" ,self.model().data(topLeft)

        row =  bottomRight.row()
        w =self.gridLayout.itemAt(row).widget()
        w.setText(self.model().data(topLeft))

    def edit(self,index,trigger,event):
        # print "==edit:",index.column(),",",index.row()
        if not index.isValid():
            return False
        if (index.column() == 0):
            return super(TtemView, self).edit(index, trigger, event)
        else:
            return False

    def indexAt(self, point):
        print "=== indexAt =="
        return QModelIndex()

    def isIndexHidden(self, index):
        print "== isIndexHidden ==="
        return False

    def horizontalOffset(self):
        # print "horizontalOffset"
        return self.horizontalScrollBar().value()

    def moveCursor(self, cursorAction, modifiers):
        current = self.currentIndex()
        return current

    def resizeEvent(self, event):
        # self.updateGeometries()
        pass

    def rows(self, index):
        print "rows"
        return self.model().rowCount(self.model().parent(index))

    def vmWidgetClicked(self):
        # self.sender()
        print " vmWidgetClicked, text =  ",self.sender().text()

    ''' 插入行'''
    def rowsInserted(self, parent, start, end):
        super(TtemView, self).rowsInserted(parent, start, end)
        print  "rowsInserted"
        print  parent.row(),":", start,",",end

        for i in range(end - start +1):
            last = self.gridLayout.count()
            x = self.gridLayout.count() % 4  # 第x列
            y = self.gridLayout.count() / 4  # 第y行
            print x,",",y

            index = self.model().index(start, 0, self.rootIndex())
            text = self.model().data(index)

            pushBtn = QPushButton(text)
            self.connect(pushBtn,SIGNAL("clicked()"),self.vmWidgetClicked)
            self.gridLayout.addWidget(pushBtn,y,x,1,1)

            # row =  bottomRight.row()
            # w =self.gridLayout.itemAt(row).widget()
            # w.setText(self.model().data(topLeft))


        # for (int row = start; row <= end; ++row)
        #         QModelIndex index = model()->index(row, 1, rootIndex());
        #         double value = model()->data(index).toDouble();
        #
        #         if (value > 0.0)
        #                 totalValue += value;
        #                 validItems++;

        # QAbstractItemView::rowsInserted(parent, start, end);

    ''' 删除行'''
    def rowsAboutToBeRemoved(self, parent, start, end):
        print  "rowsAboutToBeRemoved"

        super(TtemView, self).rowsAboutToBeRemoved(parent, start, end)

        # for i in range(end - start + 1):
        print "---- del ---", start,",", end

        if  start <= 0 or end < start:
            return

        widget_list = self.gridLPopToList()

        tmp_list = range(start -1 ,end)
        tmp_list.reverse()
        for i in tmp_list:
            if  i < widget_list.__len__():
                print "pop  %s" % i
                w = widget_list.pop(i)
                w.close()

        #     # if self.gridLayout.count() > 0:
        #         # last = self.gridLayout.count() - 1
        #         # w = self.gridLayout.takeAt(i).widget()
        #         # w.setParent(None)
        #         # w.close()
        self.gridLInsertFromeList(widget_list)

    def gridLPopToList(self):
        widget_list = []
        for i in  range(self.gridLayout.count()):
            last = self.gridLayout.count() -1
            w = self.gridLayout.takeAt(last).widget()
            w.setParent(None)
            widget_list.insert(0,w)

        return widget_list

    '''从list 中,插入gridlayout'''
    def gridLInsertFromeList(self,widget_list):
        for w in widget_list:
            self.gridLayout.addWidget(w)


    def verticalOffset(self):
        return self.verticalScrollBar().value()

    def visualRect(self, index):
        # print "visualRect  " * 3
        # print "visualRect : " * 3 ,  index.row(),":",index.column()
        return QRect()
