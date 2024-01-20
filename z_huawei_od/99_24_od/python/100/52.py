# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 52
  Description :

🎃样例1
输入
2
100 95
输出
0 0
说明：
第一个小朋友身高100，站在队尾位置，向队首看，没有比他身高的小朋友，所以输出第一个值为0，第二个小朋友站在队首，前面也没有比他身高的小朋友，所以输出第二个值为0



🎃样例2
输入
8
123 124 125 121 119 122 126 123
输出
1 2 6 5 5 6 0 0
说明：
123的好朋友是1位置上的124
124的好朋友是2位置上的125
125的好朋友是6位置上的126
以此类推

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 11:36
-------------------------------------------------
"""


def solution(n, highs):
    """
    题目含义：给一组小朋友身高，当前排列顺序中，比自己身高高的第一个小朋友就是自己的朋友，输出朋友的位置
    """
    results = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if highs[j] > highs[i]:
                results[i] = j
                break

    return results


if __name__ == "__main__":
    n = int(input())
    highs = list(map(int, input().split(" ")))
    print(" ".join([str(i) for i in solution(n, highs)]))
