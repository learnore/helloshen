# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 50
  Description :

输入
3
5
1 2 3 4 5
输出
6
说明
—次最多执行3个任务，最少耗时6s


示例2
输入输出示例仅供调试，后台判题数据─般不包含示例
输入
4
5
5 4 1 1 1
输出
5

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 10:04
-------------------------------------------------
"""
import math


def solution(deal_task, n, tasks):
    """
    处理逻辑
    1、小于等于 deal_task 的任务本次就可以处理完
    2、大于 deal_task 的任务，tasks[i]-deal_task 的任务，放在之后执行，以此类推
    """
    result = 0

    cur_task = 0
    for i in tasks:
        if cur_task != 0:
            i += cur_task

        if i <= deal_task:
            cur_task = 0
        else:
            cur_task = i - deal_task

        result += 1

    if cur_task:
        result += math.ceil(cur_task/deal_task)

    return result


if __name__ == "__main__":
    deal_task = int(input())
    n = int(input())
    tasks = list(map(int, input().split(" ")))

    print(solution(deal_task, n, tasks))
