# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_sort
  Description : list.sort()     本方法不会新建一个列表
                sorted(list)    新建一个列表作为返回值

  Author      : chenyushencc@gmail.com
  date        : 2022/4/27 8:01
-------------------------------------------------
"""

if __name__ == '__main__':
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(fruits.sort())    # None
    print(sorted(fruits))   # ['apple', 'banana', 'grape', 'raspberry']
    print(sorted(fruits, reverse=True))             # ['raspberry', 'grape', 'banana', 'apple']
    print(sorted(fruits, key=len))                  # ['apple', 'grape', 'banana', 'raspberry']
    print(sorted(fruits, key=len, reverse=True))    # ['raspberry', 'banana', 'apple', 'grape']
