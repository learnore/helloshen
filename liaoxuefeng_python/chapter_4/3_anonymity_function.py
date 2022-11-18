# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 3_anonymity_function
  Description : lambda  匿名函数
  Author      : chenyushencc@gmail.com
  date        : 2022/11/18 16:44
-------------------------------------------------
"""

if __name__ == "__main__":
    """ 关键字 lambda 表示匿名函数，冒号前面的x表示函数参数 """
    def build(x, y):
        return lambda: x * x + y * y

    print(build(1, 2))      # <function build.<locals>.<lambda> at 0x0000026F419C29E0>
    print(build(1, 2)())    # 5
