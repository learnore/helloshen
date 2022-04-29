# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_bisect
  Description : bisect 模块包含两个主要函数，bisect 和 insort，两个函数都利用二分查找算法来在有序
                序列中查找或插入元素。
  Author      : chenyushencc@gmail.com
  date        : 2022/4/29 8:06
-------------------------------------------------
"""
from bisect import bisect

if __name__ == '__main__':
    """
    * bisect(haystack, needle)
    * 在 haystack（干草垛）里搜索 needle（针）的位置
    * 其中 haystack 必须是一个有序的序列
    """
    haystack = [12, 21, 33, 41]     # 干草垛
    needle = 12                     # 针
    index = bisect(haystack, needle)
    print(index)
    haystack.insert(index, 55)
    print(haystack)

