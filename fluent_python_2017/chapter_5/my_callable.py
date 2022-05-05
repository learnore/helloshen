# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_callable
  Description : callable()  判断对象能否调用，最安全的方法是使用内置的 callable() 函数

                Python 数据模型文档列出了 7 种可调用对象:
                1 用户定义的函数
                    使用 def 语句或 lambda 表达式创建。
                2 内置函数
                    使用 C 语言（CPython）实现的函数，如 len 或 time.strftime。
                3 内置方法
                    使用 C 语言实现的方法，如 dict.get。
                4 方法
                    在类的定义体中定义的函数。
                5 类
                    调用类时会运行类的 __new__ 方法创建一个实例，然后运行 __init__ 方法，初始化实
                    例，最后把实例返回给调用方。因为 Python 没有 new 运算符，所以调用类相当于调用
                    函数。（通常，调用类会创建那个类的实例，不过覆盖 __new__ 方法的话，也可能出现
                    其他行为。）
                6 类的实例
                    如果类定义了 __call__ 方法，那么它的实例可以作为函数调用。
                7 生成器函数
                    使用 yield 关键字的函数或方法。调用生成器函数返回的是生成器对象。

  Author      : chenyushencc@gmail.com
  date        : 2022/5/5 22:57
-------------------------------------------------
"""

if __name__ == '__main__':
    print([callable(abs), callable(str), callable(13)])
