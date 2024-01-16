# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 30
  Description :

🎃样例1
输入
bb12-34aa
输出
-31
说明：
1+2+ (-34)=-31


🎃样例2
输入
bb1234aa
输出
10
说明：
1+2+3+4=10


  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/16 22:43
-------------------------------------------------
"""


def solution(s):
    """ 将字符串数字部分相加 """
    results = 0

    sb = ""     # 用于存 负数
    for i in s:
        if i == "-":
            sb += "-"
        elif sb and ord("0") <= ord(i) <= ord("9"):
            sb += i
        elif sb and (ord("0") >= ord(i) or ord(i) >= ord("9")):
            results += int(sb)
            sb = ""
        elif ord("0") <= ord(i) <= ord("9"):
            results += int(i)

    return results


if __name__ == "__main__":
    s = input().strip()
    results = solution(s)
    print(results)
