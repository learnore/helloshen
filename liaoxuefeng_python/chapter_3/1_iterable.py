# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1_iterable
  Description : 迭代 & 生成器 & 迭代器
                凡是可作用于for循环的对象都是Iterable类型
                凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
                集合数据类型如 list、dict、str 等是 Iterable 但不是 Iterator，不过可以通过 iter() 函数获得一个 Iterator 对象。

  Author      : chenyushencc@gmail.com
  date        : 2022/11/14 21:44
-------------------------------------------------
"""
from typing import Iterator

if __name__ == "__main__":
    """ I 迭代 """
    from collections.abc import Iterable
    print(isinstance('abc', Iterable))      # True      str 可迭代

    """ II 生成器 generator: 一边循环一边计算 """
    g = (x * x for x in range(10))    # () 创建一个generator
    L = [x * x for x in range(10)]    # [] list
    print(next(g))      # 0

    """
    # 这里，最难理解的就是generator函数和普通函数的执行流程不一样。
    # 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    # generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。 
    """
    def odd():      # odd不是普通函数，而是generator函数
        print('step 1')
        yield (1)
        print('step 2')
        yield (3)
        print('step 3')
        yield (5)

    o = odd()
    next(o)     # step 1
    next(o)     # step 2
    next(o)     # step 3
    # next(o)     # 抛出异常    StopIteration
    """ 请务必注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。 """

    next(odd())     # step 1
    next(odd())     # step 1
    next(odd())     # step 1
    """ 原因在于odd()会创建一个新的generator对象，上述代码实际上创建了3个完全独立的generator，对3个generator分别调用next()当然每个都会返回第一个值。 """

    """ III 迭代器 """
    """ 
    # 可以直接作用于for循环的数据类型有以下几种：
    # 一类是集合数据类型，如list、tuple、dict、set、str等；
    # 一类是generator，包括生成器和带yield的generator function
    """
    """
    # 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
    # 把list、dict、str等Iterable变成Iterator可以使用iter()函数
    # Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。 
    # Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
    """
    print(isinstance([], Iterable))     # True
    print(isinstance([], Iterator))     # False
    print(isinstance(iter([]), Iterator))   # True

    # ------------------------------------------
    # Python的for循环本质上就是通过不断调用next()函数实现的
    for x in [1, 2, 3, 4, 5]:
        pass
    """ 完全等价于 """
    # 首先获得Iterator对象:
    it = iter([1, 2, 3, 4, 5])
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break
    # ------------------------------------------
