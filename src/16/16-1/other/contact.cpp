#include "contact.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSqlRecord>
#include <QCompleter>
#include <QtCore>
#include <QDebug>
Contact::Contact(QWidget *parent) :
    QWidget(parent)
{
    //创建一个QSqlTableModel
    _model = new QSqlTableModel;
    //手动提交
    _model->setEditStrategy(QSqlTableModel::OnManualSubmit);
    //_model->setEditStrategy(QSqlTableModel::OnFieldChange);

    // _model->setTable("book_category");
    _model->setTable("student_table");
    _model->select();
    
    _view = new QTableView;  
    _view->setModel(_model);  /* view里面设置model */

    connect(_model, SIGNAL(dataChanged(QModelIndex,QModelIndex)),
            this, SLOT(slotModelDataChanged(QModelIndex,QModelIndex)));

    // set Layout
    QVBoxLayout* vBox = new QVBoxLayout(this);
    vBox->addWidget(_view);
    QHBoxLayout* hBox = new QHBoxLayout;
    vBox->addLayout(hBox);
 
    //添加add
    hBox->addWidget(_filter = new QLineEdit, 1);

    QPushButton * _add=new QPushButton("Add");
    _add->setObjectName("Add");
    hBox->addWidget(_add);

    QPushButton * _del=new QPushButton("Del");
    _del->setObjectName("Del");
    hBox->addWidget(_del);
    hBox->addWidget(_reset=new QPushButton("Reset"));
    hBox->addWidget(_submit=new QPushButton("Submit"));

    //connect(_del, &QPushButton::clicked, [&](){});
    //connect(_reset, &QPushButton::clicked, [&](){});
    
    //模糊查询
    connect(_filter, SIGNAL(textChanged(QString)),
            this, SLOT(slotFilterChanged(QString)));

    slotModelDataChanged(QModelIndex(), QModelIndex());

    QMetaObject::connectSlotsByName(this);
}

void Contact::on_Add_clicked()
{
     QSqlRecord record = _model->record();
    _model->insertRecord(-1, record);
}

void Contact::on_Del_clicked()
{
        _model->submitAll();
}

void Contact::slotFilterChanged(QString filter)
{
    if(filter.isEmpty())
    {
        _model->setFilter("");
        _model->select();
        return;
    }
    //  username like filter or password like  filter .......
    QSqlRecord record = _model->record();
    QString modelFilter;
    qDebug()<< record.count();

    for(int i=0; i<record.count(); ++i)
    {
        if(i!=0)
        {
            modelFilter += " or ";
        }
        QString field = record.fieldName(i);
        QString subFilter = QString().sprintf("%s like '%%%s%%'", field.toUtf8().data(), filter.toUtf8().data());
        // qDebug() << subFilter;
 
        modelFilter += subFilter;
    }

    qDebug() << modelFilter;
    _model->setFilter(modelFilter);
    _model->select();
}
 
void Contact::slotModelDataChanged(QModelIndex,QModelIndex)
{
    QStringList strList;
    for(int i=0; i<_model->rowCount(); ++i)
    {
        QSqlRecord record = _model->record(i);
        for(int j=0; j<record.count(); ++j)
        {
            QVariant var = record.value(j);
            if(var.isNull()) continue;
            strList << var.toString();
        }
    }
    qDebug() << strList;
    QCompleter* completer=new QCompleter(strList);
    _filter->setCompleter(completer);
}
