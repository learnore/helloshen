# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 12
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/8 16:09
-------------------------------------------------
"""


def max_pizza_size(n, sizes):
    total_slices = sum(sizes)
    half_slices = total_slices // 2

    dp = [0] * (half_slices + 1)

    for size in sizes:
        for j in range(half_slices, size-1, -1):
            dp[j] = max(dp[j], dp[j - size] + size)

    return dp[half_slices] * 2


if __name__ == "__main__":
    # 示例测试
    n = 5
    sizes = [8, 2, 10, 5, 7]
    result = max_pizza_size(n, sizes)
    print(result)  # 输出 19

