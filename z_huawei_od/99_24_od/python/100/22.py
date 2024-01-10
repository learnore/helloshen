# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 22
  Description : 简单逻辑
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/10 10:37
-------------------------------------------------
"""


def turn_four_to_five(number):
    total_fee, jifeibiao = 0, 0

    for i in range(number):
        if jifeibiao == number:
            return total_fee
        total_fee += 1
        jifeibiao += 1

        if "4" in str(jifeibiao):           # 计费表，遇4变5
            jifeibiao = int(str(jifeibiao).replace("4", "5"))

    return -1


if __name__ == "__main__":
    jifeibiao = int(input())
    print(turn_four_to_five(jifeibiao))
