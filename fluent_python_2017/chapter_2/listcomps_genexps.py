# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : listcomps_genexps
  Description : listcomps = list comprehension 列表推导
                genexps = generator expression 生成器表达式
  Author      : chenyushencc@gmail.com
  date        : 2022/4/23 11:00
-------------------------------------------------
"""

if __name__ == '__main__':
    """
    * Python2.x 列表推导会有变量泄漏的问题，Python3 则不会再有这个问题
    """
    x = 'my precious'
    dummy = [x for x in 'ABC']  # 列表推导
    print(x)    # Python2.x 变量泄漏 - 控制台会打印 'C'

    """
    * 原以为 map/filter 组合起来用要比列表推导快一些，Alex Martelli 却说不一定——至少在这个例子中不一定
    """
    symbols = '$¢£¥€¤'
    beyond_ascii_1 = [ord(s) for s in symbols if ord(s) > 127]              # 列表推导
    print(beyond_ascii_1)
    beyond_ascii_2 = list(filter(lambda c: c > 127, map(ord, symbols)))     # map/filter 组合
    print(beyond_ascii_2)

    """
    * 列表推导的作用只有一个：生成列表。如果想生成其他类型的序列，生成器表达式就派上了用场。
    * 生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。
    * 生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已。
    """
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    t_shirts = [(color, size) for size in sizes for color in colors]
    print(t_shirts)

    """
    * tips
    * 用到生成器表达式之后，内存里不会留下一个有 6 个组合的列表，因为生成器表达式会在每次 for 循环运行时才生成一个组合。
    * 
    * 生成器表达式逐个产出元素，从来不会一次性产出一个含有 6 个 T 恤样式的列表，避免额外的内存占用。
    """
    for t_shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(t_shirt)

