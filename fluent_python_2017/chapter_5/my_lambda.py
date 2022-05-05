# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_lambda
  Description : 匿名函数 lambda
                lambda 关键字在 Python 表达式内创建匿名函数。
                然而，Python 简单的句法限制了 lambda 函数的定义体只能使用纯表达式。换句话说，
                lambda 函数的定义体中不能赋值，也不能使用 while 和 try 等 Python 语句。


                                Lundh 提出的 lambda 表达式重构秘笈

                如果使用 lambda 表达式导致一段代码难以理解，Fredrik Lundh 建议像下面这样重构。
                (1) 编写注释，说明 lambda 表达式的作用。
                (2) 研究一会儿注释，并找出一个名称来概括注释。
                (3) 把 lambda 表达式转换成 def 语句，使用那个名称来定义函数。
                (4) 删除注释。
                这几步摘自“Functional Programming HOWTO”（https://docs.python.org/3/howto/functional.
                html），这是一篇必读文章。

                lambda 句法只是语法糖：与 def 语句一样，lambda 表达式会创建函数对象。这是 Python
                中几种可调用对象的一种。

  Author      : chenyushencc@gmail.com
  date        : 2022/5/5 22:49
-------------------------------------------------
"""


if __name__ == '__main__':
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda word: word[::-1]))      # 使用 lambda 表达式反转拼写，然后依此给单词列表排序