# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 62
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/20 12:42
-------------------------------------------------
"""


def solution(n, x, products, touziedu):
    """
    解题方式：
    1、m 个理财产品 总资产n元，
    2、最大总风险x = 2个投资风险之和
    3、投资回报 = 投资额*回报率
    """
    result = []
    return result


if __name__ == "__main__":
    m, n, x = map(int, input().strip().split(" "))
    huibaolv = list(map(int, input().strip().split(" ")))
    fengxianzhi = list(map(int, input().strip().split(" ")))
    products = zip(huibaolv, fengxianzhi)
    touziedu = list(map(int, input().strip().split(" ")))

    print(" ".join(solution(n, x, products, touziedu)))
