# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : collections_abc
  Description : 广义上的映射类型
  Author      : chenyushencc@gmail.com
  date        : 2022/5/2 12:28
-------------------------------------------------
"""
from collections import abc


if __name__ == '__main__':
    my_dict = {}
    print(isinstance(my_dict, abc.Mapping))     # collections.abc 广义上的映射类型
    print(type(my_dict))

    """
    * hash() 用于获取取一个对象（字符串或者数值等）的哈希值
    * 不可散列的    []
    * 可散列的      str、bytes、数值类型、frozenset
    """
    tt = (1, 2, (30, 40))
    print(hash(tt))
    try:
        tl = (1, 2, [30, 40])
        print(hash(tl))
    except TypeError:
        print("""
        Traceback (most recent call last):
            File "D:\soft_code\PyCharm 2021.2.3\workspace\helloshen\fluent_python_2017\chapter_3\collections_abc.py", line 22, in <module>
                print(hash(tl))
        TypeError: unhashable type: 'list'
        """)
    tf = (1, 2, frozenset([30, 40]))
    print(hash(tf))

    """
    * dict 5种表达方式
    """
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print(a == b == c == d == e)

