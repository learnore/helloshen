# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : test
  Description : 向量类
  Author      : chenyushencc@gmail.com
  date        : 2022/4/21 23:29
-------------------------------------------------
"""

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    """
    * Python 对象的一个基本要求就是它得有合理的字符串表示形式， 
    * __repr__ 和 __str__ 来满足这个要求，
    * 前者方便我们调试和记录日志，后者则是给终端用户看的
    """

    """
    * __repr__() 字符串表示形式之一，自定义输出实例化对象时的信息
    * <类名 + object + 内存地址>
    * <Vector object at 0x10e100070
    """
    def __repr__(self):
        # return 'Vector(%r, %r)' % (self.x, self.y)    # %r 用来替代所代表的对象
        return 'Vector({}, {})'.format(self.x, self.y)  # str.format()

    """
    * __str__() 字符串表示形式之二，注意 return 的类型：
    * TypeError: __str__ returned non-string (type float)
    """
    def __str__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)        # hypot() 返回欧几里德范数 sqrt(x*x + y*y)。PS：已知两边 求 第三边 的长度

    def __bool__(self):
        # return bool(self.x or self.y)
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar):              # scalar adj 纯量的; 标量的; 无向量的 / n 数量，标量
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(1, 3)
    v2 = Vector(2, 1)

    v = v1 + v2

    print(v)
    print(abs(v))
    print(abs(v * 3))
    print(v * 3)
    print(str(v * 3))
