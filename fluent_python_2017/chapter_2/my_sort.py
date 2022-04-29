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
    print(fruits.sort())    # None,因为是对 fruits 自身排序，所以没有输出
    print(sorted(fruits))   # 默认顺序排序 ['apple', 'banana', 'grape', 'raspberry']
    print(sorted(fruits, reverse=True))             # 逆序排序 ['raspberry', 'grape', 'banana', 'apple']
    print(sorted(fruits, key=len))                  # 长度顺序排序 ['apple', 'grape', 'banana', 'raspberry']
    print(sorted(fruits, key=len, reverse=True))    # 长度逆序排序 ['raspberry', 'banana', 'apple', 'grape']


 