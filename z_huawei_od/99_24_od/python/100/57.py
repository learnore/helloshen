# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 57
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/20 10:15
-------------------------------------------------
"""


def solution(n, lucky_num, input_list):
    """
    解题方案
    1、扫描整个行动坐标，遇到特殊数字，正方向+1负方向-1
    2、每次行动记录保存当前的最大坐标 max_x
    """
    max_x, cur_x = 0, 0
    for i in input_list:
        if i == lucky_num and lucky_num < 0:
            i -= 1
        elif i == lucky_num and lucky_num > 0:
            i += 1

        cur_x += i
        max_x = max(max_x, cur_x)

    return max_x


if __name__ == "__main__":
    n = int(input().strip())
    lucky_num = int(input().strip())
    input_list = list(map(int, input().strip().split(" ")))

    print(solution(n, lucky_num, input_list))
