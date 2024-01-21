# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 56
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 14:49
-------------------------------------------------
"""


def solution(m, input_list, n):
    """
    解决方案
    1、去重 set 集合
    2、排序
    3、前N和 + 后N和
    4、附加条件：重叠返回-1
    """
    input_list = list(set(input_list))
    input_list.sort(key=lambda x:x, reverse=False)

    m = len(input_list)         # 去重后重新计算个数

    if input_list[m-n] <= input_list[n-1]:      # 有重叠
        return -1

    result = sum(input_list[0:n]) + sum(input_list[m-n-1: m])
    return result


if __name__ == "__main__":
    m = int(input().strip())
    input_list = list(map(int, input().split(" ")))
    n = int(input().strip())

    print(solution(m, input_list, n))
