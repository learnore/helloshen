# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 24
  Description : 
  Summary     : 1、根据 n m 计算出最少的列数 n //= m； n += 1
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/15 9:54
-------------------------------------------------
"""
import math

directions = [
    (0, 1),     # 右移
    (1, 0),     # 下移
    (0, -1),    # 左移
    (-1, 0)     # 上移
]


def generate_spiral_matrix(n, m):
    """ n 数字的个数，m 矩阵的行数 """
    result = []

    col = math.ceil(n/m)            # 细节：12/4 = 3.0

    for _ in range(m):
        temp = []
        for _ in range(col):
            temp.append("*")

        result.append(temp)

    # 起点
    x, y = 0, 0
    result[x][y] = "1"

    count = 2
    cur_direction = 0
    while count <= n:
        # 前进
        x += directions[cur_direction % 4][0]
        y += directions[cur_direction % 4][1]

        if 0 <= x < m and 0 <= y < col and result[x][y] == "*":       # 只要不是越界 和 *，按照当前方向前进
            result[x][y] = str(count)  # 填充
            count += 1

        else:
            x -= directions[cur_direction % 4][0]
            y -= directions[cur_direction % 4][1]

            cur_direction += 1          # 转方向

    return result


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    results = generate_spiral_matrix(n, m)
    for i in range(len(results)):
        print(" ".join(results[i]))
