# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 23
  Description : 
  Summary     : 1、将 k 转为 m 进制 = km
                2、看 km 中有多少个 n 的字符串
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/15 9:15
-------------------------------------------------
"""


def count_lucky_number(k, n, m):
    """
    k表示：该客人购买的物品价值(以十进制计算的价格)
    n表示：该客人的幸运数字
    m表示：该客人所在国度的采用的进制
    """
    result = 0

    # km = int(str(k), m)       # 这是将 m 进制的 k 转为 int 10进制
    # 将 k 转为 m 进制，结果为 km

    # 通用反转
    km = ""
    while k > 0:
        km = str(k%m) + km
        k //= m

    for i in str(km):
        if i == str(n):
            result += 1

    return result


if __name__ == "__main__":
    k, n, m = map(int, input().split(" "))
    print(count_lucky_number(k, n, m))
