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
    """ 输入的字符串处理 """
    str.strip()  # 去除字符串的前后空格
    str.replace(" ", "")  # 去除字符串内所有的空格

    a = int(input())                                # 一行 1个输入
    A = list(map(int, input().split()))             # 一行多个输入，并变 list

    """
    多个输入
    
    题目要求，换行表示继续输入时，以ctrl+z表示输入结束
    如“输入，第1行表示期望申请的内存字节数，输入的2-N行表示...”，所以，不确定 N 的大小
    """
    while True:
        try:
            offset, size = map(int, input().split())        # 一般以 ctrl + z 结束输入
        except EOFError:
            break

    """
    多个输入
    题目要求，输入结尾不带回车换行
    """
    while True:
        input_str = input().strip()
