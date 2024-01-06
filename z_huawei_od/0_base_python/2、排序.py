# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 排序
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2024/1/4 19:29
-------------------------------------------------
"""

if __name__ == "__main__":
    heights = [110, 100, 110, 100]
    heights.sort(reverse=False)     # False 从小到大排序
    heights.sort(reverse=True)      # True 从大到小排序
    print(heights)

    weights = [32, 50, 40, 50]

    # 创建学生列表，元素为元组 (编号, 身高, 体重)
    students = [(i + 1, heights[i], weights[i]) for i in range(len(heights))]

    # 按照身高、体重、编号的顺序进行排序
    students.sort(key=lambda x: (x[1], x[2], x[0]), reverse=False)      # x[1] 越大

    # 提取排序后的学生编号
    result = [student[0] for student in students]
    print(result)       # [2, 3, 1, 4]