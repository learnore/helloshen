# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 19
  Description :

🎃题目描述
给定一个二维数组M行N列，二维数组里的数字代表图片的像素，为了简化问题，仅包含像素1和5两种像素,每种像素代表一个物体，2个物体相邻的格子为边界，求像素1代表的物体的边界个数

像素1代表的物体的边界指与像素5相邻的像素1的格子，边界相邻的属于同一个边界，相邻需要考虑8个方向(上，下，左，右，左上，左下，右上，右下)

其他约束：
地图规格约束为:
0<M<100
0<N<100

1、如下图，与像素5的格子相邻的像素1的格子(0，0) 、(0，1) 、(0，2) 、(1，0) 、(1，2) 、(2，0) 、(2，1) 、(2，2) 、(4，4)、(4，5) 、(5，4) 为边界，另(0，0)、(0，1)、(0，2) 、(1，0)、(1，2) 、(2，0)、(2，1) 、(2，2) 相邻，为1个边界，(4，4) 、(4，5) 、(5，4) 相邻，为1个边界，所以下图边界个数为2
在这里插入图片描述

2、如下图，与像素5的格子相邻的像素1的格子(0，0) 、(0，1) 、(0，2)、(1，0) 、(1，2)、(2，0)、(2,1) 、(2，2)、(3，3)、(3，4)、(3，5)，(4，3)(4，5)、(5，3)、(5，4)、(5，5) 为边界，另这些边界相邻，所以下图边界个数为1
在这里插入图片描述

注：(2，2) 、(3，3) 相邻

🎃输入输出
输入
第一行，行数M，列数N
第二行开始，是M行N列的像素的二维数组，仅包含像素1和5

输出
像素1代表的物体的边界个数
如果没有边界输出0 (比如只存在像素1，或者只存在像素5)

🎃样例1
输入
6 6
1 1 1 1 1 1
1 5 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 5
输出
2


🎃样例2
输入
6 6
1 1 1 1 1 1
1 5 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 5 1
1 1 1 1 1 1
输出
1

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 16:03
-------------------------------------------------
"""
from queue import Queue


def solution(x, y, graph):
    """
    解题思路：
    1、找到 5，将其8个方向的1改为0
    2、遍历到0时，边界个数 +1，将该点作为起点，开始8个方向的 BFS 遍历
    """
    for i in range(x):
        for j in range(y):
            if graph[i][j] == 5:
                # 将该点周围8个位置标记为0
                if 0 <= i-1 < x and 0 <= j-1 < y:
                    graph[i-1][j-1] = 0

                if 0 <= i-1 < x and 0 <= j < y:
                    graph[i-1][j] = 0

                if 0 <= i-1 < x and 0 <= j+1 < y:
                    graph[i-1][j+1] = 0

                if 0 <= i < x and 0 <= j - 1 < y:
                    graph[i][j-1] = 0

                if 0 <= i < x and 0 <= j+1 < y:
                    graph[i][j+1] = 0

                if 0 <= i+1 < x and 0 <= j-1 < y:
                    graph[i+1][j-1] = 0

                if 0 <= i + 1 < x and 0 <= j < y:
                    graph[i+1][j] = 0

                if 0 <= i + 1 < x and 0 <= j+1 < y:
                    graph[i+1][j+1] = 0

    count = 0
    for i in range(x):
        for j in range(y):
            if graph[i][j] == 0:
                count += 1
                bfs(graph, i, j, x, y)

    return count


def bfs(graph, i, j, x, y):
    """
    从该点进行广度优先遍历，是0的，改为-1
    """
    queue = Queue()
    queue.put((i, j))
    graph[i][j] = -1

    while not queue.empty():
        i, j = queue.get()

        # 将该点四面八方为0的都设置为-1
        if 0 <= i - 1 < x and 0 <= j - 1 < y and graph[i - 1][j - 1] == 0:
            graph[i - 1][j - 1] = -1
            queue.put((i - 1, j - 1))

        if 0 <= i - 1 < x and 0 <= j < y and graph[i - 1][j] == 0:
            graph[i - 1][j] = -1
            queue.put((i - 1, j))

        if 0 <= i - 1 < x and 0 <= j + 1 < y and graph[i - 1][j + 1] == 0:
            graph[i - 1][j + 1] = -1
            queue.put((i - 1, j+1))

        if 0 <= i < x and 0 <= j - 1 < y and graph[i][j - 1] == 0:
            graph[i][j - 1] = -1
            queue.put((i, j - 1))

        if 0 <= i < x and 0 <= j + 1 < y and graph[i][j + 1] == 0:
            graph[i][j + 1] = -1
            queue.put((i, j + 1))

        if 0 <= i + 1 < x and 0 <= j - 1 < y and graph[i + 1][j - 1] == 0:
            graph[i + 1][j - 1] = -1
            queue.put((i+1, j - 1))

        if 0 <= i + 1 < x and 0 <= j < y and graph[i + 1][j] == 0:
            graph[i + 1][j] = -1
            queue.put((i + 1, j))

        if 0 <= i + 1 < x and 0 <= j + 1 < y and graph[i + 1][j + 1] == 0:
            graph[i + 1][j + 1] = -1
            queue.put((i + 1, j+1))


if __name__ == "__main__":
    x, y = map(int, input().split(" "))
    graph = [list(map(int, input().strip().split(" "))) for _ in range(x)]

    print(solution(x, y, graph))
