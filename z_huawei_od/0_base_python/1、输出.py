# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1、输出
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 21:35
-------------------------------------------------
"""

if __name__ == "__main__":
    # 1
    i = "1"
    target = "2"
    print(i, target, sep=" ")

    # 2 用空格代替换行
    """
    空格输出
    1 2 3
    """
    for student in [1, 2, 3]:
        print(student, end=" ")

    # 3
    """
    换行输出
    1
    2
    3
    """
    for student in [1, 2, 3]:
        print(student)
