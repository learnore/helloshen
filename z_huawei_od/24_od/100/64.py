# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 64
  Description : 一维dp，动态规划

🎃样例1
输入
50
输出
122106097


🎃样例2
输入
3
输出
2

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/12 10:18
-------------------------------------------------
"""


dp_1 = [1]       # dp 备忘录
dp_2 = [1, 1, 1, 2]


def count_jump_ways_1(n):

    """
    一般方法，四部曲 = base case + 选择 + 状态 + dp备忘录种元素的含义
    n 个台阶，返回爬这n个台阶的方法数
    """
    # base case
    if n < 0:
        return 0        # 不合法的值都返回 0 种方法

    # 表示该 n 已经被计算过，加入了备忘录，那就直接获取该值即可
    if dp_1[n] != -2:
        return dp_1[n]

    # 选择：1 和 3 就是猴子的选择
    # 状态：台阶的数量在变化
    if n-3 >= 0:        # 此时，n-1必大于0
        dp_1[n] = count_jump_ways_1(n - 1) + count_jump_ways_1(n - 3)
    elif n-1 >= 0:      # 此时，n-3必小于0，所以可以不用判断
        dp_1[n] = count_jump_ways_1(n - 1)

    return dp_1[n]


def count_jump_ways_2(n):
    """ 优化一：改为自底向上 """
    if n <= 3:
        return dp_2[n]

    # 以下是 n >= 4
    if dp_2[n] != -2:       # 如果备忘录 dp 已经有相关的值了，那就直接返回即可，避免重复计算
        return dp_2[n]

    dp_2[n] = count_jump_ways_2(n-1) + count_jump_ways_2(n-3)
    return dp_2[n]


def count_jump_ways_3(n):
    """ 优化二：自底向上基础上，再优化空间：滚动更新 dp 里面的数据 """
    # 初始值 dp[1, 1, 1, 2]
    if n == 0:
        return 1

    dp_i_1, dp_i_2, dp_i_3 = 1, 1, 2

    for i in range(4, n+1):
        temp_res = dp_i_3 + dp_i_1

        # 滚动更新
        dp_i_1 = dp_i_2
        dp_i_2 = dp_i_3
        dp_i_3 = temp_res

    return dp_i_3


if __name__ == "__main__":
    n = int(input())

    """ 方法一 """
    # 填充备忘录
    for _ in range(1, n+1):
        dp_1.append(-2)
    result_1 = count_jump_ways_1(n)
    # print(dp_1)

    """ 方法二 """
    # 填充备忘录
    for _ in range(4, n+1):        # 细节 n+1
        dp_2.append(-2)
    result_2 = count_jump_ways_2(n)

    """ 方法三 """
    result_3 = count_jump_ways_3(n)

    print(result_1)
    print(result_2)
    print(result_3)

