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
from PyQt4.QtCore import QModelIndex, QRect
from PyQt4.QtGui import QAbstractItemView, QRegion,QGridLayout, \
    QLabel,QPushButton,QWidget


class TtemView(QAbstractItemView):
    def __init__(self, parent=None):
        super(TtemView, self).__init__(parent)
        self.gridLayout = QGridLayout(self)
        # self.lable = QLabel("testLabel",self)
        # self.lable.setMinimumSize(100,100)
        # self.gridLayout.addWidget(self.lable,0,0,1,1)

        # last = self.gridLayout.count() - 1
        # self.gridLayout.addWidget(QPushButton("testLabel1"),0,0,1,1)
        # self.gridLayout.addWidget(QPushButton("testLabel2"),0,1,1,1)
        #
        # self.listw =[]
        # last = self.gridLayout.count() - 1
        # w =self.gridLayout.takeAt(last).widget()
        # self.listw.append(w)
        #
        # # last = self.gridLayout.count() - 1
        # # w =self.gridLayout.takeAt(last).widget()
        # # print type(w) , "#" *10
        # # self.listw.append(w)
        # # print self.listw.__len__()
        #
        # self.gridLayout.addWidget(self.listw[0],0,0,1,1)
        # self.gridLayout.addWidget(self.listw[1],0,1,1,1)
        # print self.listw.__len__()
        # #
        # # print "*"  * 100
        # self.listw[:] = []
        # print self.listw.__len__()

    # public:
    #     QRect visualRect(const QModelIndex &index) const
    #     void scrollTo(const QModelIndex &index, ScrollHint hint = EnsureVisible)
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

        w =self.gridLayout.itemAt(0).widget()
        w.setText(self.model().data(topLeft))

        # last = self.gridLayout.count() - 1
        # w =self.gridLayout.itemAt(last).widget()
        # w.setText("1234abc")


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

    def mousePressEvent(self, event):
        # print "mousePressEvent"
        pass
        # QAbstractItemView::mousePressEvent(event);
        # origin = event->pos();
        # if (!rubberBand)
        #         rubberBand = new QRubberBand(QRubberBand::Rectangle, viewport());
        # rubberBand->setGeometry(QRect(origin, QSize()));
        # rubberBand->show();

    def mouseMoveEvent(self, event):
        pass
        # if (rubberBand)
        #         rubberBand->setGeometry(QRect(origin, event->pos()).normalized());
        # QAbstractItemView::mouseMoveEvent(event);

    def mouseReleaseEvent(self, event):
        super(TtemView, self).mouseReleaseEvent(event)
        # if (rubberBand)
        #         rubberBand->hide();
        # viewport()->update();

    def moveCursor(self, cursorAction, modifiers):

        current = self.currentIndex()
        return current

    def resizeEvent(self, event):
        # self.updateGeometries()
        pass

    def rows(self, index):
        print "rows"
        return self.model().rowCount(self.model().parent(index))

    # 插入行
    def rowsInserted(self, parent, start, end):
        super(TtemView, self).rowsInserted(parent, start, end)
        print  "rowsInserted"
        for i in range(end - start +1):
            last = self.gridLayout.count()
            self.gridLayout.addWidget(QPushButton("...."),0,last,1,1)

        # for (int row = start; row <= end; ++row)
        #         QModelIndex index = model()->index(row, 1, rootIndex());
        #         double value = model()->data(index).toDouble();
        #
        #         if (value > 0.0)
        #                 totalValue += value;
        #                 validItems++;

        # QAbstractItemView::rowsInserted(parent, start, end);

    # 删除行
    def rowsAboutToBeRemoved(self, parent, start, end):
        print  "rowsAboutToBeRemoved"

        super(TtemView, self).rowsAboutToBeRemoved(parent, start, end)

        for i in range(end - start + 1):
            print "---- del ---"

            if self.gridLayout.count() > 0:
                last = self.gridLayout.count() - 1
                w = self.gridLayout.takeAt(last).widget()
                w.setParent(None)
                w.close()

        # for (int row = start; row <= end; ++row)
        #
        #         QModelIndex index = model()->index(row, 1, rootIndex());
        #         double value = model()->data(index).toDouble();
        #         if (value > 0.0)
        #                 totalValue -= value;
        #                 validItems--;
        #
        # QAbstractItemView::rowsAboutToBeRemoved(parent, start, end);

    def scrollContentsBy(self, dx, dy):
        self.viewport().scroll(dx, dy)

    def scrollTo(self, index, ScrollHint):
        pass
        # QRect area = viewport()->rect();
        # QRect rect = visualRect(index);
        #
        # if (rect.left() < area.left())
        #         horizontalScrollBar()->setValue(
        #                 horizontalScrollBar()->value() + rect.left() - area.left());
        # else if (rect.right() > area.right())
        #         horizontalScrollBar()->setValue(
        #                 horizontalScrollBar()->value() + qMin(
        #                         rect.right() - area.right(), rect.left() - area.left()));
        #
        # if (rect.top() < area.top())
        #         verticalScrollBar()->setValue(
        #                 verticalScrollBar()->value() + rect.top() - area.top());
        # else if (rect.bottom() > area.bottom())
        #         verticalScrollBar()->setValue(
        #                 verticalScrollBar()->value() + qMin(
        #                         rect.bottom() - area.bottom(), rect.top() - area.top()));
        # update();

    def setSelection(self, rect, command):
        print "setSelection"

    # def updateGeometries(self):
    #     pass
    #     # horizontalScrollBar()->setPageStep(viewport()->width());
    #     # horizontalScrollBar()->setRange(0, qMax(0, 2*totalSize - viewport()->width()));
    #     # verticalScrollBar()->setPageStep(viewport()->height());
    #     # verticalScrollBar()->setRange(0, qMax(0, totalSize - viewport()->height()));

    def verticalOffset(self):
        return self.verticalScrollBar().value()

    def visualRect(self, index):
        print "visualRect" * 10
        print "itemRect : ",  index.row()
        return QRect()

        # rect = self.itemRect(index)
        # if (rect.isValid()):
        #     return QRect(rect.left() - self.horizontalScrollBar().value(),
        #                  rect.top() - self.verticalScrollBar().value(),
        #                  rect.width(), rect.height())
        # else:
        #     return rect

    def visualRegionForSelection(self, selection):
        print "visualRegionForSelection"

        ranges = selection.count()

        if (ranges == 0):
            return QRect()

        region = QRegion()
        # for (int i = 0; i < ranges; ++i)
        #         QItemSelectionRange range = selection.at(i);
        #         for (int row = range.top(); row <= range.bottom(); ++row)
        #                 for (int col = range.left(); col <= range.right(); ++col)
        #                         QModelIndex index = model()->index(row, col, rootIndex());
        #                         region += visualRect(index);
        return region
