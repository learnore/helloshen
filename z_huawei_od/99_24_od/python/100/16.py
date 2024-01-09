# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 16
  Description :

--------- 用例 ---------
输入
30 12 25 8 19
输出
15

--------- 用例 ---------
输入
10 12 25 8 19 8 6 4 17 19 20 30
输出
-1

--------- 用例 ---------
输入
10 12 25 8 19 8 6 4
输出
25

--------- 用例 ---------
输入
100
输出
13

  Summary     : 1、“机器人一个小时中只能在一个仓库中搬砖”超过8个仓库，必返回-1
                2、一小时补充一次能量格，如：每小时补充 15 个能量格子，也就是说一小时能搬 15 个砖
                3、要从 1 开始，找最小的能量格，防止出现给一个超大用例的情况
  Author      : chenyushencc@gmail.com
  date        : 2024/1/9 10:37
-------------------------------------------------
"""
import math


def can_complete(bricks, energy):
    """
    检查给定的能量是否足以让机器人在规定时间内搬运所有砖块。
    :param bricks: 砖块堆的列表，每个数字代表一个砖块堆的砖块数量
    :param energy: 机器人每小时的能量值（每小时可以搬运的砖块数量）
    :return: 布尔值，能否在规定时间内搬运所有砖块
    """
    total_hours = 0  # 总共需要的小时数
    for brick in bricks:
        # total_hours += -(-brick // energy)  # 使用天花板除法计算每堆砖块需要的小时数
        total_hours += math.ceil(brick / energy)        # math 公式向上取整

    return total_hours <= 8  # 如果总小时数小于等于规定时间 8，则返回True


def find_min_energy(bricks):
    """
    找到机器人搬运所有砖块所需的最小能量值。
    :param bricks: 砖块堆的列表
    :return: 最小的有效能量值
    """
    if len(bricks) > 8:
        return -1

    total_bricks = sum(bricks)  # 所有砖块的总和
    for energy in range(1, total_bricks + 1):  # 从1开始逐一尝试每个能量值
        if can_complete(bricks, energy):  # 如果当前能量值有效
            return energy  # 返回当前的能量值作为最小有效能量值

    return -1  # 如果找不到有效的能量值，返回-1


if __name__ == "__main__":
    bricks = list(map(int, input().strip().split(" ")))
    min_energy = find_min_energy(bricks)
    print(f"{min_energy}")
