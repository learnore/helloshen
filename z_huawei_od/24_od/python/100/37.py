# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 37
  Description :

🎃样例1
输入
15
输出
3 5
说明：
因数分解后，找到两个素数3和5，使得3*5=15，按从小到大排列后，输出3 5


🎃样例2
输入
27
输出
-1 -1
说明：
通过因数分解，找不到任何素数，使得他们的乘积为27，输出-1 -1

  Summary     : 1、1不是素数
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 20:08
-------------------------------------------------
"""


def solution(n):
    """ 将一个数拆成2个素数相乘 """
    results = [-1, -1]
    if n == 1:
        return results

    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and is_prime(i) and is_prime(n//i):
            results = [i, n//i]
            break

    return results


def is_prime(n):
    """ 判断n是否是素数：除了1和本身，不能被其他数整除 """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    n = int(input())
    print(" ".join([str(i) for i in solution(n)]))
