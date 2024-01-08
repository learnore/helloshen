# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 11
  Description :

----------------- 用例 --------------------
输入
3 3
1 0 1
0 0 0
0 1 0
输出
9
说明：
土地上的旗子为1, 其坐标分别为(0,0), (2,1)以及(0,2), 为了覆盖所有旗子，矩阵需要覆盖的横坐标为0和2,纵坐标为0和2,所以面积为9,即(2-0+1)*(2-0+1)=9

----------------- 用例 --------------------
输入
3 3
1 0 2
0 0 0
0 3 4
输出
1
说明:
不存在成对的旗子，返回1

----------------- 用例 --------------------
输入
3 3
1 0 1
0 0 0
0 2 0
输出
3

----------------- 用例 --------------------
输入
3 4
1 0 1 0
0 2 0 1
0 2 0 0
输出
8


  Summary     : 1、第一个是行数，第二个是列数
                2、逐行扫描
                3、用字典dict，记录每个数字的矩形的四个点
                4、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/8 13:17
-------------------------------------------------
"""


def calculate_largest_area(m, n, grid):
    # 创建一个字典来存储 每个数字旗子 的最小矩阵边界
    flags = {}

    for i in range(m):
        for j in range(n):
            flag = grid[i][j]
            # 如果当前位置有旗子
            if flag != 0:
                if flag in flags:
                    # 更新旗子的边界
                    flags[flag]["min_i"] = min(flags[flag]["min_i"], i)
                    flags[flag]["max_i"] = max(flags[flag]["max_i"], i)     # 注意是 max
                    flags[flag]["min_j"] = min(flags[flag]["min_j"], j)
                    flags[flag]["max_j"] = max(flags[flag]["max_j"], j)     # 注意是 max
                else:
                    # 如果旗子是第一次出现，初始化其边界
                    flags[flag] = {
                        "min_i": i,
                        "max_i": i,
                        "min_j": j,
                        "max_j": j
                    }
    # 遍历所有旗子，计算它们的最小覆盖矩阵面积，并找到最大值
    max_area = 0
    for key, value in flags.items():
        area = (flags[key]["max_i"] - flags[key]["min_i"] +1) * (flags[key]["max_j"] - flags[key]["min_j"] +1)      # 别忘了+1
        max_area = max(max_area, area)

    # 如果没有旗子，则返回1
    return max_area if max_area > 0 else 1


if __name__ == "__main__":
    # 读取输入数据
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        # 一行数据
        row = list(map(int, input().split()))
        grid.append(row)
    # 计算要分配的土地面积并输出
    result = calculate_largest_area(m, n, grid)
    print(result)
