# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : python_bin_turn
  Description : 进制转换 + 位运算
                参考博客：https://blog.csdn.net/weixin_45503064/article/details/127546793
  Author      : chenyushencc@gmail.com
  date        : 2023/2/2 22:42
-------------------------------------------------
"""

if __name__ == "__main__":
    """ 1 进制转换：将其他进制统一用 int 转为 10进制 """
    print(int("10", 2))     # 2
    print(int("10", 8))     # 8
    print(int("10", 16))    # 16

    """ 一般反转：2 8 16 进制，转为 10进制，python 有内置函数 """
    print(bin(2))  # 0b10
    print(oct(8))  # 0o10
    print(hex(16))  # 0x10

    """ 通用反转 """
    k = 10      # 待转数据，10进制
    m = 4       # 4进制
    km = ""     # 结果
    while k > 0:
        km = str(k % m) + km
        k //= m
    print(f"将10进制的 k 转为 {m}进制的结果是 ({km}){m}")     # 将10进制的 k 转为 4进制的结果是 (22)4

    """ 另外，为了方便记忆，将 ASCII 码相关的的函数一并整理 """
    print(ord("A"))     # 65
    print(ord("a"))     # 97
    print(ord("0"))     # 48
    print(chr(65))      # A

    """
    小进制 <—— 十进制（通过十进制过滤转换） ——> 大进制
    """
    print(hex(int("1111", 2)))      # 0xf
    print(bin(int("f", 16)))        # 0b1111

    """ 2 位运算   &     |   ^     ~   <<    >> """
    # & 按位与运算符，要都是 1 才是 1
    print(1 & 0)        # 0
    print(1 & 1)        # 1
    print(0 & 0)        # 0

    # | 按位或运算符，只要有 1 就是 1
    print(1 | 0)  # 1
    print(1 | 1)  # 1
    print(0 | 0)  # 0

    # ^ 按位异或运算符，要两个不同时才为 1
    print(1 ^ 0)  # 1
    print(1 ^ 1)  # 0
    print(0 ^ 0)  # 0

    # ~ 按位取反运算符，对数据的每个二进制位取反，即把1变为0，把0变为1
    print(bin(~1))      # 0b 0 01 ——> 按位取反 0b 1 10    (-0b10)
    print(bin(~-3))      # 0b 0 011 ——> 按位取反 0b 1 100  (-0b100)

    # >>：右移动运算符
    print(3 >> 1)       # 1

    # <<：左移动运算符
    print(3 << 1)       # 6

    """
    set
    """
    # set 集合位运算
    print(set({1,2,3,4}) & set({2,3,4,5}))      # {2, 3, 4}
    # == 因为 set 和 dict 在内存中所存储的规则都是用的 hash 方式，所以开一段内存后，将数值按照相同的规则存储，肯定就是相等的啦
    print(set({2,3,4}) == set({3,4,2}))     # True      == 会调用默认的 __eq__() 方法
    print(dict({"a": 1, "b": 2, "c": 3}) == dict({"b": 2, "a": 1, "c": 3}))     # True
    # set 就算写的一样也是不同的id哦
    print(set({2,3,4}) is set({3,4,2}))     # False
    print(set({2,3,4}) is set({2,3,4}))     # False

