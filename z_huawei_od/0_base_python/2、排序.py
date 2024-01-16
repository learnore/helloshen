# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 排序
  Description :
  Summary     : 1、小技巧，负号
                2、100 T27
  Author      : chenyushencc@gmail.com
  date        : 2024/1/4 19:29
-------------------------------------------------
"""

if __name__ == "__main__":
    """
    排序
    """
    # sorted
    print(sorted({0: 1, 2: 2, 1: 3}.items(), reverse=True))  # [(2, 2), (1, 3), (0, 1)]      按照 key
    # 原来时字典！原来时字典！原来时字典！注意这里 sorted 后的数据，返回的是一个数组里面包裹的是元组哦!!是元组哦!!是元组哦!!是元组哦!!是元组哦!!
    print(sorted({0: 1, 2: 1, 1: 3}.items(), key=lambda x: (x[1], -x[0]), reverse=True))  # [(1, 3), (0, 1), (2, 1)]
    # 使用两个元素进行升序排序，在第一个元素升序的情况下，第二个元素也升序排序
    print(sorted([(6, 4), (6, 8), (6, 7), (7, 1)], key=lambda x: (x[0], x[1])))  # [(6, 4), (6, 7), (6, 8), (7, 1)]
    # 小技巧：在第一个元素升序的情况下，第二个元素的 负号（反方向）升序/即就是降序排序即可
    print(sorted([(6, 4), (6, 8), (6, 7), (7, 1)], key=lambda x: (x[0], -x[1])))  # [(6, 8), (6, 7), (6, 4), (7, 1)]

    # sort
    sort1 = [(2, 43), (1, 65), (7, 42)]
    sort1.sort(key=lambda x: x[0])
    print(sort1)        # [(1, 65), (2, 43), (7, 42)]

    """ --------------------------------------------------------- """
    heights = [110, 100, 110, 100]
    weights = [32, 50, 40, 50]

    heights.sort(reverse=False)     # False 从小到大排序
    heights.sort(reverse=True)      # True 从大到小排序
    print(heights)

    # 创建学生列表，元素为元组 (编号, 身高, 体重)
    students = [(i + 1, heights[i], weights[i]) for i in range(len(heights))]

    # 按照身高、体重、编号的顺序进行排序
    students.sort(key=lambda x: (x[1], x[2], x[0]), reverse=False)      # x[1] 越大

    # 提取排序后的学生编号
    result = [student[0] for student in students]
    print(result)       # [2, 3, 1, 4]


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

