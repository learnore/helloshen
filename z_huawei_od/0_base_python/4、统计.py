# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 4、统计
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2024/1/6 10:33
-------------------------------------------------
"""
from collections import Counter             # collections 模块

if __name__ == "__main__":
    # 示例数据
    data = [1, 2, 3, 1, 2, 1, 4, 5, 4, 3, 2, 1]

    # 使用Counter统计元素个数
    count_result = Counter(data)
    max_valus = max(count_result.values())
    print(max_valus)                # 统计中，数量最大是多少

    print(count_result.total())     # 数组的元素个数/统计的所有个数

    # 输出统计结果
    for element, count in count_result.items():     # element, count in count_result.items()
        print(f"{element}: {count}")
