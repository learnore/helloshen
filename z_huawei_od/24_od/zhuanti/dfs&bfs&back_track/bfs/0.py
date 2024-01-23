# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 0 bfs 框架
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 17:00
-------------------------------------------------
"""
from queue import Queue


def bfs(graph, mom, baby, n):
    """ 单向，母亲朝着孩子方向前进 """
    # todo 初始化参数
    result = 0

    queue = Queue()                 # ******
    queue.put( )

    visited = set()                 # ******
    visited.add( )                  # 加入首次的参数
    while not queue.empty():        # ******
        temp_x, temp_y, temp_steps, temp_candies = queue.get()          # ******
        # todo 逻辑

    return result


if __name__ == "__main__":
    print("chenyushen")
