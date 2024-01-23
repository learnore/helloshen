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


def array_catch_the_same(arrays):
    """ [[], []. []]数组去重 """
    """ tuple - set - list """
    result_set = set(tuple(i) for i in arrays)      # 先将内部的数组 tuple([])，再用 set 去重
    result = [list(s) for s in result_set]          # 恢复成数组

    # [list(i) for i in set(tuple(i) for i in arrays)]
    return result


if __name__ == "__main__":
    check_even_odd(7)

