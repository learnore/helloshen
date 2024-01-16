# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 29
  Description :

🎃样例1
输入
[1,2,3,4,5,6,7,8,9],4,3
输出
13


🎃样例2
输入
[1,2,2,2,2,3,4,1,2,2,3,4],4,4
输出
12

  Summary     : 1、是个数学公式
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/16 20:15
-------------------------------------------------
"""


def solution(nums, jump, left):
    """ 返回剩余 left 个数字 """
    cur_index = 1       # 按照常规的，从1开始计数
    while len(nums) > left:
        cur_index = (cur_index+jump+1) % len(nums) -1           # 最后，在数组中的下标位置，在正常的位置 -1 即可
        nums.pop(cur_index)

    return nums


if __name__ == "__main__":
    x, y = map(str, input().split("],"))
    nums = list(map(int, x.replace("[", "").split(",")))
    jump, left = map(int, y.split(","))

    results = solution(nums, jump, left)
    print(sum(results))
