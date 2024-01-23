# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 58
  Description :

🎃样例1
输入
alolobo
输出
6


🎃样例2
输入
looxdolx
输出
7


🎃样例3
输入
bcbcbc
输出
6

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/20 10:26
-------------------------------------------------
"""
from collections import Counter


def solution(input_str):
    """
    解题思路：
    1、判断字符串中 o 的个数
    2、偶数个 o ，则最长就是整个字符串的长度 len(*)
    3、奇数个 o ，是个环，所以最长是 len(*)-1
    """
    counter = Counter(input_str)
    if counter["o"] % 2 == 0:      # 偶数个
        return len(input_str)
    else:
        return len(input_str)-1


if __name__ == "__main__":
    print(solution(input().strip()))
