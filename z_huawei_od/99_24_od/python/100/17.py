# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 17
  Description :

--------- 样例1 --------
输入
4 10
1 1
2 1
3 1
4 -2
输出
12
1
2
3
4
5
6
7
8

-------- 样例2 --------
输入
2 4
0 1
2 -2
输出
4
1
2
3
4
5
6

-------- 样例3 --------
输入
5 10
1 1
2 2
3 3
4 4
5 -5
输出
45
1
2
3
4
5
6
7
8
9

-------- 样例4 --------
输入
3 6
0 1
2 -2
4 4
输出
10
1
2
3
4
5
6
7

-------- 样例5 --------
输入
2 8
1 1
3 -3
输出
12
1
2
3
4
5
6

-------- 样例6 --------
输入
4 10
0 2
2 -2
4 4
6 -6
输出
20
1
2
3
4
5
6
7
8

-------- 样例7 --------
输入
10 20
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 -10
输出
515
1
2
3
4
5
6
7
8
9
10
11
12
13
14

-------- 样例8 --------
输入
6 15
0 1
2 -2
4 4
6 -6
8 8
10 -10
输出
51
1
2
3
4
5
6
7
8
9
10

-------- 样例9 --------
输入
8 18
1 1
4 -4
6 6
8 -8
9 9
12 -12
14 14
17 -17
输出
77
1
2
3
4
5
6
7
8
9
10
11
12

-------- 样例10 --------
输入
7 14
1 1
3 3
5 5
7 -7
9 9
11 -11
13 13
输出
67

  Summary     : 1、用例的X不相同，且只能增加
                2、X offsetY 表示在当前的运行轨迹上开始偏移（看题目图片）
                    比如当前在Y=1上运行，那么 3 offset2 则表示
                    运动到 X=3 时，继续向Y的正方向偏移2位，也就是从X=3开始，在Y=3上向X正方向直线运行
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/9 11:46
-------------------------------------------------
"""


def cul_area(E, instructions):
    prevX, prevY, area = 0, 0, 0
    for key, value in enumerate(instructions):
        x, offsetY = value
        area += abs(x - prevX) * abs(prevY)
        prevX = x
        prevY += offsetY
    area += abs(E - prevX) * abs(prevY)
    return area


if __name__ == "__main__":
    N, E = map(int, input().split())  # 输入N和E

    instructions = []
    for i in range(N):
        x, offsetY = map(int, input().split())  # 输入每条指令的x和offsetY
        instructions.append((x, offsetY))
    print(cul_area(E, instructions))
