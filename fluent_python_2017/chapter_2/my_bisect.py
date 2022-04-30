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
import sys
import bisect
import random


if __name__ == '__main__':
    """
    * bisect(haystack, needle)
    * 在 haystack（干草垛）里搜索 needle（针）的位置
    * 其中 haystack 必须是一个有序的序列
    """
    haystack = [12, 21, 33, 41]     # 干草垛
    needle = 12                     # 针
    index = bisect.bisect(haystack, needle)
    print(index)
    haystack.insert(index, 55)
    print(haystack)


# --------------------------------------------------------------------


HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    """
    运行结果（bisect_fn = bisect.bisect_left）
    
    DEMO: bisect_left
    haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
    31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
    30 @ 13      |  |  |  |  |  |  |  |  |  |  |  |  |30
    29 @ 12      |  |  |  |  |  |  |  |  |  |  |  |29
    23 @  9      |  |  |  |  |  |  |  |  |23
    22 @  9      |  |  |  |  |  |  |  |  |22
    10 @  5      |  |  |  |  |10
     8 @  4      |  |  |  |8 
     5 @  2      |  |5 
     2 @  1      |2 
     1 @  0    1 
     0 @  0    0 
    """

    """
    运行结果（bisect_fn = bisect.bisect_right）

    DEMO: bisect_right
    haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
    31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
    30 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |30
    29 @ 13      |  |  |  |  |  |  |  |  |  |  |  |  |29
    23 @ 11      |  |  |  |  |  |   |  |  |  |  |23
    22 @  9      |  |  |  |  |  |  |  |  |22
    10 @  5      |  |  |  |  |10
     8 @  5      |  |  |  |  |8 
     5 @  3      |  |  |5 
     2 @  1      |2 
     1 @  1      |1 
     0 @  0    0 
    """
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


# --------------------------------------------------------------------


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """
    F   < 60
    D   [60, 70)
    C   [70, 80)
    B   [80, 90)
    A   90 >
    :param score:
    :param breakpoints:
    :param grades:
    :return:

    * bisect.bisect 返回的索引从 1 开始
    * i = 1/2/3/4
    * grades 是一个 len() = 5 的字符串，可以取到 0/1/2/3/4
    *
    * bisect.bisect         ['F', 'D', 'F', 'C', 'B', 'A', 'A']
    * bisect.bisect_right   ['F', 'D', 'F', 'C', 'B', 'A', 'A']
    * bisect.bisect_left    ['F', 'F', 'F', 'D', 'B', 'B', 'A']
    * 
    * 综上所述：
    * bisect.bisect == bisect.bisect_right
    """
    i = bisect.bisect_right(breakpoints, score)       # bisect.bisect = bisect.bisect
    return grades[i]


if __name__ == '__main__':
    print([grade(score) for score in [-10, 60, 33, 70, 89, 90, 100]])


# --------------------------------------------------------------------


if __name__ == '__main__':
    """
    * insort(seq, item) 把变量 item 插入到序列 seq 中，并能保持 seq 的升序顺序
    """
    SIZE = 7

    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%2d -> ' % new_item, my_list)

