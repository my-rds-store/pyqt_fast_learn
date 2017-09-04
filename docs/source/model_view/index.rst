#################
16. 模型/视图编程
#################

16.1 模型/视图架构
==================

16.1.1 组成部分
---------------

1). 模型
^^^^^^^^
2). 视图
^^^^^^^^
3). 委托
^^^^^^^^

16.1.2 简单的例子
-----------------

.. literalinclude:: ../../../src/16/16-1/modelView1/modelView1.py
    :language: python
    :encoding: utf-8


16.1.3 小试牛刀
-----------------

1). QCompleter自动补全
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../src/16/16-1/complete/main.py
    :language: python
    :encoding: utf-8


常用的方法

    * void setMaxVisibleItems(int maxItems)   设置最大显示数目
    * void setCaseSensitivity(Qt::CaseSensitivity caseSensitivity)  设置是否区分大小写

     
    +----------------------+-------+---------------------+
    |                      | value |                   --|
    +======================+=======+=====================+
    | Qt::CaseInsensitive  |  0    | (默认) 大小写不敏感 |
    +----------------------+-------+---------------------+
    | Qt::CaseSensitive    |  1    |   大小写敏感        |
    +----------------------+-------+---------------------+



* void setModelSorting(ModelSorting sorting)  设置排序方式

    QCompleter::ModelSorting取值如下：

    +------------------------------------------+---------+----------------------------+
    |                                          |  value  |                            |
    +==========================================+=========+============================+
    | QCompleter::UnsortedModel                |    0    | 该模型是未排序             |
    +------------------------------------------+---------+----------------------------+
    | QCompleter::CaseSensitivelySortedModel   |    1    | 该模型是大小写敏感排序     |
    +------------------------------------------+---------+----------------------------+
    | QCompleter::CaseInsensitivelySortedModel |    2    | 该模型是大小写不敏感排序的 |
    +------------------------------------------+---------+----------------------------+


3). 自动完成的QLineEdit(非使用QCompleter版)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../src/16/16-1/CompleteLineEdit_py/completelineEdit.py
    :language: python
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-1/CompleteLineEdit_py/main.py
    :language: python
    :encoding: utf-8



16.2 模型类
===========

16.2.1 基本概念
---------------

.. literalinclude:: ../../../src/16/16-2/modeView1.py
    :language: python
    :encoding: utf-8


16.2.2 创建新的模型
-------------------

1.   
^^^^^^^^^^^^^^

.. literalinclude:: ../../../src/16/16-3/stringlistmodel.py
    :language: python
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-3/main.py 
    :language: python
    :encoding: utf-8

2.   
^^^^^^^^^^^^^^


.. literalinclude:: ../../../src/16/16-4/stringlistmodel.py
    :language: python
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-4/main.py
    :language: python
    :encoding: utf-8

3.   
^^^^^^^^^^^^^^

.. literalinclude:: ../../../src/16/16-5/stringlistmodel.py
    :language: python
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-5/main.py
    :language: python
    :encoding: utf-8


16.3 视图类
===========

16.3.1 基本概念
---------------

16.3.2 处理项目选择
-------------------


.. literalinclude:: ../../../src/16/16-6/mainwindow.py
    :language: python
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-6/main.py
    :language: py
    :encoding: utf-8



**QTiemSelectionModel::Toggle**

.. literalinclude:: ../../../src/16/16-7/mainwindow.py
    :language: python
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-7/main.py
    :language: py
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-8/mainwindow.py
    :language: py
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-8/main.py
    :language: py
    :encoding: utf-8



16.4 委托类
===========

16.4.1 基本概念
---------------

16.4.2 自定义委托
-----------------

.. literalinclude:: ../../../src/16/16-9/mainwindow.py
    :language: py
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-9/spinboxdelegate.py
    :language: py
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-9/main.py
    :language: py
    :encoding: utf-8


16.5 项目视图的便捷类
=====================

16.5.1 QListWidget
------------------

16.5.2 QTreeWidget
------------------

16.5.3 QTableWidget
-------------------

16.6 在项目视图中启用拖放
=========================

16.6.1 在便捷类中启用拖放
-------------------------

.. literalinclude:: ../../../src/16/16-11/main.py
    :language: py
    :encoding: utf-8


16.6.2 在模型/视图类中启用拖放
------------------------------

.. literalinclude:: ../../../src/16/16-12/main.py
    :language: py
    :encoding: utf-8


16.7 其他内容
=============

16.7.1 代理模型
---------------

.. literalinclude:: ../../../src/16/16-13/mainwindow.py
    :language: py
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-13/main.py
    :language: py
    :encoding: utf-8

16.7.2 数据-窗口映射器
----------------------

.. literalinclude:: ../../../src/16/16-14/mainwindow.py
    :language: py
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-14/main.py
    :language: py
    :encoding: utf-8

16.8 小结
=========

