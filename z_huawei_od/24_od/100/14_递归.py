# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 14
  Description : 递归

------------- 用例 ----------------
输入
7#6$5#12
输出
226


  Summary     : 1、获取一个字符串中最后一个 "#" 字符的下标：
                        str.rindex("#")
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/8 17:33
-------------------------------------------------
"""


def mars_language(input_str):
    """
    递归拦截：没有 # $ 时，就是一个数字  int(input_str)
    """
    if "#" in input_str:
        idx = input_str.rindex("#")     # 找到最后一个 # 的下标
        left = input_str[:idx]
        right = input_str[idx+1:]
        return 2*mars_language(left) + 3*mars_language(right) + 4

    elif "$" in input_str:
        idx = input_str.rindex("$")  # 找到最后一个 # 的下标
        left = input_str[:idx]
        right = input_str[idx + 1:]
        return 3*mars_language(left) + mars_language(right) + 2

    else:
        # base case
        return int(input_str)


if __name__ == "__main__":
    while True:         # 题目要求，输入结尾不带回车换行
        input_str = input().strip()
        print(mars_language(input_str))
