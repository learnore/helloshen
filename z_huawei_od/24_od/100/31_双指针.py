# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 31
  Description :

🎃样例0
输入
6
3 1 2 5 7 9
8
输出
3
说明：
3、5组成一队，1、7一队，9自己一队，输出3

🎃样例1
输入
5
3 1 5 7 9
8
输出
3
说明：
3、5组成一队，1、7一队，9自己一队，输出3


🎃样例2
输入
7
3 1 5 7 9 2 6
8
输出
4
说明：
3、5组成一队，1、7一队，9自己一队, 2、6一队，输出4


🎃样例3
输入
3
1 1 9
8
输出
1
说明：
9自己一队，输出1

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/16 23:02
-------------------------------------------------
"""


def solution(n, capacity, sum_capacity):
    """ 按照从小到大排序 """
    results = 0

    capacity.sort()
    # 先将独个能完成任务的，排除掉
    while True:
        if capacity[-1] >= sum_capacity:
            results += 1
            capacity.pop()
        else:
            break

    left, right = 0, len(capacity)-1        # 数组的左右下标指针
    while left <= right:
        if capacity[left] + capacity[right] >= sum_capacity:
            results += 1
            left += 1
            right -= 1
        else:
            left += 1

    return results


if __name__ == "__main__":
    n = int(input())
    capacity = list(map(int, input().split(" ")))
    sum_capacity = int(input())

    print(solution(n, capacity, sum_capacity))
