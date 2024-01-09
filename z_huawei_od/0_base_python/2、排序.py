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

    """
    小技巧： 
    x[1]要从大到小排序
    x[0].lower() 又要从小到大排序
    则将 x[1] 添上负号，然后统一从小到大排序即可
    """
    [(123, "asd"), (123, "wer")].sort(key=lambda x: (-x[1], x[0].lower()), reverse=False)


    """
    其他处理方式
    """
    # 报错 TypeError: sort() takes no positional arguments
    # flights.sort(lambda x: (x[:2], int(x[2:])), reverse=False)
    # 改用 sorted(list, key=lambda x:(x[])) 格式
    """
    解释：
    x[:2] 前2位按照从小到大排序
    int(x[2:]) 后几位先变成int后从小到大排序
    """
    sorted_list = sorted(["CA3385", "CZ6678", "SC6508", "DU7523", "HK4456", "MK0987"],
                         key=lambda x: (x[:2], int(x[2:])))

