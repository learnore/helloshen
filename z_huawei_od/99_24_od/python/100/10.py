# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 10
  Description :

-------- 示例 --------
输入
XXYYXYXXYYYYYXXX
输出
2
说明：可以分割两个子串：
XXYY
XY
分割后的子串，是原字符串的连续子串

  Summary     : 1、将一个字符串分割成多个字符串
                2、尽可能多的分割出“均衡串”
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/8 12:58
-------------------------------------------------
"""


def max_number_of_balanced_substrings(s):
    count_X, count_Y, result = 0, 0, 0
    for char in s:
        if char == "X":
            count_X += 1
        else:
            count_Y += 1

        if count_X == count_Y:
            result += 1
            count_X, count_Y = 0, 0         # 重置 X Y 的计数

    return result


if __name__ == "__main__":
    print(max_number_of_balanced_substrings(input()))
