# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 15 可以组成网络的服务器 （DFS）
  Description :

🎃题目描述
在一个机房中，服务器的位置标识在n * m 的整数矩阵网格中，1 表示单元格上有服务器， 0表示没有；如果两台服务器位于同一行或者同一列中紧邻的位置，则认为它们之间可以组成一个局域网

请你统计机房中最大的局域网包含的服务器个数

🎃输入输出
输入
第一行输入两个正整数，n和m， 0<n，m<=100
之后为 n *m的二维数组，代表服务器信息

输出
最大局域网包含的服务器个数

🎃样例1
输入
2 2
1 0
1 1
输出
3
说明：
[0][0]、[1][0]、[1][1]三台服务器相互连接，可以组成局域网


🎃样例2
输入
3 3
0 1 0
0 1 1
1 1 1
输出
6


🎃样例3
输入
3 3
1 1 0
1 0 1
1 0 1
输出
4

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 12:38
-------------------------------------------------
"""


def dfs(graph, i, j, visited):
    """ dfs """
    if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]) or visited[i][j] or graph[i][j] == 0:
        return 0

    visited[i][j] = True
    count = 1
    count += dfs(graph, i+1, j, visited)
    count += dfs(graph, i-1, j, visited)
    count += dfs(graph, i, j+1, visited)
    count += dfs(graph, i, j-1, visited)

    return count


def max_local_network(graph):
    """ 根据一个表，找出连续的1的最大个数 """
    if not graph or not graph[0]:
        return 0

    max_result, x, y = 0, len(graph), len(graph[0])
    visited = [[False for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if graph[i][j] == 1 and not visited[i][j]:
                max_result = max(max_result, dfs(graph, i, j, visited))

    return max_result


if __name__ == "__main__":
    x, y = map(int, input().strip().split(" "))
    graph = [list(map(int, input().strip().split(" "))) for i in range(x)]
    print(max_local_network(graph))