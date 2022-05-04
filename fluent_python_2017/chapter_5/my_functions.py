# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_functions
  Description : 函数的 __doc__ 属性
  Author      : chenyushencc@gmail.com
  date        : 2022/5/4 22:16
-------------------------------------------------
"""


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)


def reverse(word):
    return word[::-1]


if __name__ == '__main__':
    # ----------------------------- 一等函数 -------------------------------------------
    print(factorial(42))            # 在运行时创建
    print(factorial.__doc__)        # __doc__ 属性用于生成对象的帮助文本
    print(type(factorial))

    fact = factorial                # 通过别的名称使用函数，再把函数作为参数传递
    print(fact)                     # <function factorial at 0x...>
    print(fact(5))                  # 120
    """
    * map 函数返回一个可迭代对象，里面的元素是把第一个参数（一个函数）应用到第二个参数（一个可迭代对象
    * 这里是 range(11)）中各个元素上得到的结果
    """
    print(map(factorial, range(6)))         # <map object at 0x...>    把它作为参数传给 map 函数
    print(list(map(factorial, range(6))))   # [1, 1, 2, 6, 24, 120]

    # ----------------------------- 高阶函数 map、filter、reduce -------------------------------------------

    """
    * 接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order function）
    """
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))      # ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']   若想根据单词的长度排序，只需把 len 函数传给 key 参数
    print(reverse('testing'))           # gnitset
    print(sorted(fruits, key=reverse))      # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
