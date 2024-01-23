# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 41
  Description :

🎃样例1
输入
0 5 8 9 9 10
5 0 9 9 9 8
输出
8 7
说明:
黑棋一共8口气，白棋一共7口气

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/18 15:21
-------------------------------------------------
"""


directions = [
    (-1, 0),        # 上
    (1, 0),         # 下
    (0, -1),        # 左
    (0, 1)          # 右
]

def solution(black_input, white_input):
    """
    解决方案
    ①根据坐标，输出其上下左右正确的坐标
    ②用set集合去重
    ③将去重后的合法坐标中，将已经落子的坐标去除
    ④得出最终的坐标个数即可
    """
    black_results, white_results = [], []
    black_temp, white_temp = [], []

    # 计算黑子的有效坐标
    for i in range(0, len(black_input), 2):
        x, y = black_input[i], black_input[i+1]
        black_temp.append((x, y))

        for d in directions:
            x += d[0]
            y += d[1]

            if 0 <= x <= 18 and 0 <= y <= 18:       # 是合法值
                black_results.append((x, y))

            # 恢复
            x -= d[0]
            y -= d[1]

    # 计算白子的有效坐标
    for i in range(0, len(white_input), 2):
        x, y = white_input[i], white_input[i + 1]
        white_temp.append((x, y))

        for d in directions:
            x += d[0]
            y += d[1]

            if 0 <= x <= 18 and 0 <= y <= 18:  # 是合法值
                white_results.append((x, y))

            # 恢复
            x -= d[0]
            y -= d[1]

    down = []
    down += black_temp + white_temp     # 合并已经落下的子

    # 去重
    white_results = set(white_results)
    black_results = set(black_results)

    # 将黑子、白子，自己和对方的落子的坐标相互删除掉
    for i in down:
        if i in black_results:
            black_results.remove(i)

        if i in white_results:
            white_results.remove(i)

    return len(list(black_results)), len(list(white_results))


if __name__ == "__main__":
    black = list(map(int, input().split(" ")))
    white = list(map(int, input().split(" ")))

    black, white = solution(black, white)

    print(black, end=" ")
    print(white)
