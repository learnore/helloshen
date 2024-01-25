# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 25
  Description :

---------- 用例 -------------
输入
20*19*20*
输出
tst

---------- 用例 -------------
输入
20*19*20*3
输出
tstc

---------- 用例 -------------
输入
320*19*20*
输出
ctst

---------- 用例 -------------
输入
220*19*20*
输出
btst

---------- 用例 -------------
输入
20*19*20*
输出
tst


  Summary     : 1、1-9 翻译成 a-i
                2、10*-26* 翻译成 j-z
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/15 11:42
-------------------------------------------------
"""


def decrypt(s):
    """ 翻译文字 """
    results = ""

    temp_str = ""
    for i in range(len(s)):
        if s[i] == "*":
            # 转换字符，清空临时字符串
            if len(temp_str) == 3:
                results += chr(int(temp_str[0]) + 96)
                temp_str = temp_str[1:]
            results += chr(int(temp_str) + 96)
            temp_str = ""

        elif s[i] == "1" or s[i] == "2" or temp_str:
            temp_str += s[i]

        else:       # 3-9 翻译 c-i
            # 转换字符，清空临时字符串
            results += chr(int(s[i]) + 96)
            temp_str = ""

    return results


if __name__ == "__main__":
    s = input().strip()
    result = decrypt(s)
    print(result)
