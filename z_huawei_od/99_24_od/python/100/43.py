# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 43
  Description :

用例1
输入
ace
abcde
输出
4

用例2
输入
aced
abcdefdwe
输出
6

样例3
输入
fgh
abcde
输出
-1

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/18 18:37
-------------------------------------------------
"""


def solution(s, l):
    """ 双指针，按顺序依 s 次序在 l 中查找字符 """
    result = -1
    s_point, l_point = 0, 0
    for i in range(len(l)):
        if s_point == len(s):
            return i-1
        elif l[i] == s[s_point]:
            s_point += 1

    if s_point == len(s):
        return len(l)-1

    return result


if __name__ == "__main__":
    s = input().strip()
    l = input().strip()
    print(solution(s, l))
