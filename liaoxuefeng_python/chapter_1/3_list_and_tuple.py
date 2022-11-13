# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : list_and_tuple
  Description : https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880
  Author      : chenyushencc@gmail.com
  date        : 2022/11/2 21:13
-------------------------------------------------
"""

if __name__ == "__main__":
    """ list是一种有序的集合 """
    classmates = ['Michael', 'Bob', 'Tracy']
    classmates.append('Adam')
    print(classmates)       # ['Michael', 'Bob', 'Tracy', 'Adam']
    classmates.insert(1, 'Jack')
    print(classmates)       # ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
    classmates.pop()
    print(classmates)       # ['Michael', 'Jack', 'Bob', 'Tracy']
    classmates.pop(1)
    print(classmates)       # ['Michael', 'Bob', 'Tracy']
    L = ['Apple', 123, True]
    print(L)

    """ 有序列表叫元组，tuple和list非常类似，但是tuple一旦初始化就不能修改 """
    t = (1)
    print(t)        # 1     数字
    t = (1,)
    print(t)        # (1,)  元组