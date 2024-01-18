# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 45
  Description :

🎃样例1
输入
100 10
95 96 97 98 99 101 102 103 104 105
输出
99 101 98 102 97 103 96 104 95 105


  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/18 20:07
-------------------------------------------------
"""


def solution(n, xiaoming, class_mates):
    """
    身高各不相同
    每个人的身高与小明的身高都有绝对值
    绝对值差相同时，身高矮的排在前面
    """
    # 找出每个人的身高差
    new_mates = []
    for i in class_mates:
        new_mates.append((i, abs(i-xiaoming)))

    new_mates.sort(key=lambda x: (x[1], x[0]), reverse=False)        # 按照绝对值差从小到大排序，其次按照身高从小到大排序
    return new_mates


if __name__ == "__main__":
    xiaoming, n = map(int, input().split(" "))
    class_mates = list(map(int, input().split(" ")))
    print(" ".join([str(i[0]) for i in solution(n, xiaoming, class_mates)]))
