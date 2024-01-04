# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 3、循环
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2024/1/4 20:56
-------------------------------------------------
"""

if __name__ == "__main__":
    texing_list = [1, 1, 2, 4, 5]
    yongli_list = [[1, 2, 3], [2, 3], [1, 2]]       # 数组嵌套

    # 实现元组 (yongli_list的序号, 每个yongli_list的item是texing_list下标的总和)
    results = [(i + 1, sum(texing_list[id - 1] for id in case)) for i, case in enumerate(yongli_list)]
    print(results)
