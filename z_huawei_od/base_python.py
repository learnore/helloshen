# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : base_paython
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/2/3 12:17
-------------------------------------------------
"""
import math

if __name__ == "__main__":
    """ 字符串 """
    # 数组 字符串 是可以使用 .count() 进行计数的
    print(["1", "1", "3"].count("1"))       # 2
    print("1231".count("1"))                # 2

    # 字符串左对其
    print("123".ljust(8, "0"))  # 12300000
    print("123".rjust(8, "0"))  # 00000123

    # 字符串可以取超过自身的区间，超过部分会自动忽略的
    print("123"[:100])

    # 求开根号
    print(math.sqrt(100))       # 10.0

    # print 的其他用法
    print("123", end=" 12\n")

    """ 常用数值计算 """
    # 向下取整
    print(int(3.56))        # 3
    # 向上取整
    print(math.ceil(3.25))  # 4
    # 四舍五入
    print(round(4.5), round(5.5), round(6.5), round(7.5))     # 4 6 6 8     TODO 坑-round 奇进偶舍，4 6 是偶数直接舍弃  5，7是奇数
    print(round(4.3), round(5.3), round(6.3), round(7.3))     # 4 5 6 7

    """ 排序 """
    print(sorted({0: 1, 2: 2, 1: 3}.items(), reverse=True))        # [(2, 2), (1, 3), (0, 1)]      按照 key
    print(sorted({0: 1, 2: 2, 1: 3}.items(), key=lambda x: x[1], reverse=True))     # [(1, 3), (2, 2), (0, 1)]      按照 value
