# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1_func
  Description : 函数调用
  Author      : chenyushencc@gmail.com
  date        : 2022/11/13 10:53
-------------------------------------------------
"""

if __name__ == "__main__":
    """ 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名” """
    a = abs
    print(a(-1))        # 1


    def my_abs(x):
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')     # 数据类型检查可以用内置函数isinstance()实现

        if x >= 0:
            return x
        else:
            return -x

    print(my_abs("A"))      # TypeError: bad operand type
