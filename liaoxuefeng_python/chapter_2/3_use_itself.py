# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 3_use_itself
  Description : 递归函数
                如果一个函数在内部调用自身本身，这个函数就是递归函数。
                函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
                每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出

  Author      : chenyushencc@gmail.com
  date        : 2022/11/13 11:44
-------------------------------------------------
"""


def fact1(n):
    if n == 1:
        return 1
    return n * fact1(n - 1)      # 不是尾递归，会有栈溢出的风险


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)        # 尾递归，在函数返回的时候，调用自身本身


if __name__ == "__main__":
    print(fact1(5))      # 120
    # print(fact1(1000))   # 栈溢出   RecursionError: maximum recursion depth exceeded in comparison
    """
    # 解决递归调用栈溢出的方法是通过尾递归优化
    # 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
    # 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
    """
    # TODO Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题...



