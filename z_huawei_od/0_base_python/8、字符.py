# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 8、字符
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 15:36
-------------------------------------------------
"""


def char_extend_pre1(next_hour, next_minute):
    """ 字符扩位 """
    return f"{next_hour:02d}:{next_minute:02d}"     # 不足2位的时间补0


def char_extend_pre2(test_str):
    """ 字符扩位 """
    return test_str.rjust(4, "0")


def char_extend_behind(test_str):
    """ 字符扩位 """
    return test_str.ljust(4, "0")


if __name__ == "__main__":
    print(char_extend_pre1(8, 9))                # 08:09
    print(char_extend_pre2(str(8)))              # 0008
    print(char_extend_behind(str(8)))            # 8000
