# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : bingocall
  Description : 实现了 BingoCage 类。这个类的实例使用任何可迭代对象构建，而且会在内部存
                储一个随机顺序排列的列表。调用实例会取出一个元素。
  Author      : chenyushencc@gmail.com
  date        : 2022/5/5 23:03
-------------------------------------------------
"""
import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    """
    * bingo 实例可以作为函数调用，而且内置
    * 的 callable(...) 函数判定它是可调用的对象
    """
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))