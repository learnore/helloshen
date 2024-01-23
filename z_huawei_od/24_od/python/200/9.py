# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 9
  Description : 动态规划（一维dp）
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/22 11:24
-------------------------------------------------
"""


def solution(n):
    """
    题目
    1、长度始终是正整数
    2、可以不切割，尽量少切割
    3、交易的价格 = 每根长度的乘积

    解题思路：
    分析得出，base case ：1=1，2=2，3=3，4=2+2=4=2*2（为了少切割）
    5=2+3（2*3=6）...所以，base case = 2、3、4
    步骤一：将整个x分解为 2 + 3
    步骤二：合并偶数个2，为4
    步骤三：输出答案

    输出
    空格分割，升序排序
    """
    # base case
    # if n == 4 or n == 3 or n == 2 or n == 1:
    #     return n
    #
    # if n <= 0:
    #     return 0

    # base case
    dp = [[], [1], [2], [3], [4]]
    dp += [[] for _ in range(4, n)]

    for i in range(5, n+1):
        dp[i] = dp[i - 3] + [3]         # 重点构造等式

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(" ".join(sorted([str(i) for i in solution(n)], key=lambda x: x, reverse=False)))


