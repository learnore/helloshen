# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 输入输出
  Description :


1
1 2
1 2 3
1 2
1 2 3

  Author      : chenyushencc@gmail.com
  date        : 2024/1/2 21:02
-------------------------------------------------
"""

if __name__ == "__main__":
    """ 输出 """
    # 1
    i = "1"
    target = "2"
    print(i, target, sep=" ")

    # 2 用空格代替换行
    """
    1 2 3
    """
    for student in [1, 2, 3]:
        print(student, end=" ")

    # 3
    """
    1
    2
    3
    """
    for student in [1, 2, 3]:
        print(student)


    """ 输入 """
    a = int(input())                                # 一行 1个输入
    len_a, len_b = map(int, input().split())        # 一行多个输入
    A = list(map(int, input().split()))             # 一行多个输入，并变 list

    """ 多个输入 """
    while True:
        try:
            offset, size = map(int, input().split())        # 多个
        except EOFError:
            break