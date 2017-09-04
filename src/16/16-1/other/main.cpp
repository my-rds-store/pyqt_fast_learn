#include <QApplication>
//#include "Widget05.h"
#include <QSqlDatabase>
#include <QSqlError>
#include <QDebug>
#include <QTextCodec>
#include "contact.h"

int main(int argc,char* argv[])
{
    QApplication app(argc,argv);

    // 这行代码要写在创建连接之前
    QTextCodec::setCodecForTr(QTextCodec::codecForName("UTF-8"));
    QTextCodec::setCodecForCStrings(QTextCodec::codecForName("UTF-8"));


    /*QT可以操作 QSLITE QODBC,QPLSQL 这些数据库*/
    //下面表示使用mysql数据库，因为这里的db没有用到db，所以可以把它放在main中
    //本质：在QT里面打开一个数据库之后，就会保存一个数据库连接，
    //其它的位置就可以任意使用这个全局的变量了
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("116.196.92.114");  //设置数据库所在位置
    db.setUserName("root");             //设置数据库的用户名
    db.setPassword("rootroot");         //设置数据库的密码
    db.setDatabaseName("palette_Library");  //设置数据库名称
    db.setPort(8306);

    bool bRet = db.open();        //打开数据库连接

    if(bRet == false)
    {
        //说明可以通过db.lastError()的方式得到错误信息
        qDebug() << "error open database" << db.lastError().text();
        exit(0);
    }
    qDebug() << "open database success";

    //注意Widget02要写在上面代码的下面
    Contact c;
    c.show();
    return app.exec();
}
