# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 47
  Description :

🎃样例1
输入
93 95 97 100 102 123 155
110
输出
6

🎃样例2
输入
93 95 97 100 111 123 155
110
输出
5

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/18 22:50
-------------------------------------------------
"""


def solution(input_list, xiaoming):
    """ 算法复杂度要求不超过 O(log2n) """
    left, right = 0, len(input_list)-1
    while left <= right:
        mid = left + (right - left)//2          # ********
        if input_list[mid] < xiaoming:
            left = mid +1
        elif input_list[mid] > xiaoming:
            right = mid -1

    return left +1


if __name__ == "__main__":
    input_list = list(map(int, input().split(" ")))
    xiaoming = int(input())
    print(solution(input_list, xiaoming))
