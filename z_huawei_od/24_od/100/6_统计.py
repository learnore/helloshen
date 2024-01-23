# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 6
  Description :

-------- 示例 --------
输入
10 11 21 19 21 17 21 16 21 18 15
输出
21

-------- 示例 --------
输入
1 1 1 3 3 3
输出
2

-------- 示例 --------
输入
1 3 3 3 1 1
输出
2


  Author      : chenyushencc@gmail.com
  date        : 2024/1/6 10:27
-------------------------------------------------
"""
from collections import Counter


def find_mode(input_array):
    """ 找出 """
    count_dict = Counter(input_array)           # 用 collections.Counter 语法糖
    max_count = max(count_dict.values())        # 找出最大的统计数
    modes = [element for element, count in count_dict.items() if count == max_count]     # 注意众数可能不止一种，找出最大的统计数所对应的元素

    new_array = []
    for _ in range(max_count):
        new_array.extend(modes)         # extend 合并

    return new_array


def calculate_median(new_array):
    """ 计算中位数 """
    new_array.sort()
    n = len(new_array)
    if n % 2 == 0:  # 偶数
        mid_1 = int(n/2)        # int 自带向下取整功能
        mid_2 = mid_1-1

        mid_number = (new_array[mid_1] + new_array[mid_2]) / 2

    else:
        mid = int((n-1)/2)
        mid_number = new_array[mid]

    return int(mid_number)


if __name__ == "__main__":
    input_array = list(map(int, input().split()))

    # 找到众数并构成新数组
    new_array = find_mode(input_array)

    # 计算新数组的中位数
    result = calculate_median(new_array)
    print(result)
