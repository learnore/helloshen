# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 3
  Description :

-------- 示例1 --------
输入
4
100 100 120 130
40 30 60 50
输出
2 1 3 4


  Author      : chenyushencc@gmail.com
  date        : 2024/1/3 22:19
-------------------------------------------------
"""


def sort_students(n, heights, weights):
    # 创建学生列表，元素为元组 (编号, 身高, 体重)
    students = [(i + 1, heights[i], weights[i]) for i in range(n)]

    # 按照身高、体重、编号的顺序进行排序
    students.sort(key=lambda x: (x[1], x[2], x[0]))

    # 提取排序后的学生编号
    result = [student[0] for student in students]

    return result


if __name__ == "__main__":
    n = int(input())

    heights = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    result = sort_students(n, heights, weights)

    for student in result:
        print(student, end=" ")