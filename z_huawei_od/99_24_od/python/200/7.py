# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 7
  Description : BFS 问题 - 最短路径
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/13 10:50
-------------------------------------------------
"""
from queue import Queue

# 四个可能的移动方向（上下左右）
from typing import Set

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs_1(graph, mom, baby, n):
    """ 单向，母亲朝着孩子方向前进 """
    max_candy = -1

    mom_x, mom_y = mom
    baby_x, baby_y = baby

    queue = Queue()
    queue.put((mom_x, mom_y, 0, 0))       # 将 mom 的初始状态首次加入，默认步数和糖果都是 0

    visited = set()
    visited.add(mom)
    while not queue.empty():
        temp_x, temp_y, temp_steps, temp_candies = queue.get()
        if temp_x == baby_x and temp_y == baby_y:               # 如果找到了孩子，那就看看当前获得的糖果数，取最大的
            max_candy = max(temp_candies, temp_candies)
            continue            # 找到了也就不用继续移动

        # 从当前的位置，继续上下左右移动
        for d in directions:
            temp_x += d[0]
            temp_y += d[1]

            if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n \
                    or graph[temp_x][temp_y] == -1 or (temp_x, temp_y) in visited:        # 越界、障碍物、已被访问
                temp_x -= d[0]                  # 易错，要恢复
                temp_y -= d[1]                  # 易错，要恢复
                continue

            visited.add((temp_x, temp_y))           # 访问前加入
            temp_candies += graph[temp_x][temp_y]
            queue.put((temp_x, temp_y, temp_steps + 1, temp_candies))

    return max_candy


def bfs_2(graph, mom, baby, n):
    """
    # 知道起点和终点，那就可以双向奔赴，母亲和孩子都前进
    # 起点和终点轮流扩散
    """
    max_candy = -1

    return max_candy


if __name__ == "__main__":
    n = int(input())
    graph, mom, baby = [], None, None
    for i in range(n):
        line = list(map(int, input().split(" ")))

        count = 0
        for j in line:
            if j == -3:
                mom = (i, count)
            elif j == -2:
                baby = (i, count)

            count += 1

        graph.append(line)

    # max_candies = bfs_1(graph, mom, baby, n)
    max_candies = bfs_2(graph, mom, baby, n)
    print(max_candies)
