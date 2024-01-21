# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 0、常用方法
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2024/1/6 10:54
-------------------------------------------------
"""


def check_even_odd(number):
    """
    判断一个数是偶数还是奇数
    """
    if number % 2 == 0:
        print(f"{number} 是偶数")
    else:
        print(f"{number} 是奇数")


if __name__ == "__main__":
    check_even_odd(7)

