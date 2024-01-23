# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 14
  Description :

🎃样例1
输入
12 7 2 1 1 -1 13
001000010000
001000010000
001000010000
001000010000
001000010000
001000010000
001000010000
输出
3
说明：
初始位置为(2,1)速度为(1,-1),那么13个时间单位后,经过点1的个数为3


🎃样例1
输入
12 7 2 1 1 -1 13
001000010000
001000010000
001000010000
001000010010
001000010001
001000010000
001000010000
输出
5


  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 12:06
-------------------------------------------------
"""

def solution(graph, x, y, sx, sy, t):
    """
    sx, sy      整个坐标的x y
    x, y        当前的位置
    vx, vy      需要移动的距离
    t           循环次数
    解题思路：
    1、检查当前位置是否是1，是则 result += 1
    2、开始移动
    """
    result = 0
    if graph[y][x] == "1":
        result += 1

    # x, y = 2, 1
    for i in range(t):
        x, y = x+sx, y+sy
        if graph[y][x] == "1":
            result += 1

        if x == 0 or x == len(graph[0])-1:
            sx *= -1        # **** 反射 *****
        if y == 0 or y == len(graph)-1:
            sy *= -1        # **** 反射 *****

    return result


if __name__ == "__main__":
    w, h, x, y, sx, sy, t = map(int, input().strip().split(" "))
    graph = []
    for i in range(h):
        graph.append(input().strip())

    print(solution(graph, x, y, sx, sy, t))
