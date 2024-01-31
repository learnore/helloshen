# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : BFS 框架
  Description :

from queue import Queue


def bfs(start, target, n):
    # 初始化参数 result、queue、visited
    result = 0

    queue = Queue()                 # ******
    queue.put( )

    visited = set()                 # ******
    visited.add( )                  # 加入首次的参数

    # 开始广度优先遍历
    while not queue.empty():        # ******
        cur = queue.get()             # ******

        # 向周围扩散，将结点加入队列中
        for i in range(n):

            # 在这里判断是否到达终点
            if cur == target:
                return

            # 将 cur 周围的结点加入队列
            queue.put( )

    return result

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 17:00
-------------------------------------------------
"""

if __name__ == "__main__":
    print("chenyushen")
