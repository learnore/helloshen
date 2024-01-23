# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 33
  Description :

🎃样例1
输入
3
1 1 1
输出
0
说明：
选出1 1 1，得到 0，最终数组转换为 []，最后没有剩下银块，返回0


🎃样例2
输入
3
3 7 10
输出
1

🎃样例3
输入
7
3 7 10 1 2 3 4
输出
1

  Summary     : 1、要先从大到小怕排序，3个为一组，不足3个时就准备输出了
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 15:15
-------------------------------------------------
"""

def solution(n, input_list):
    """
    按照规则进行融化银首饰  x <= y <= z
    x=y=z       0
    x=y<z       z-y
    x<y=z       y-x
    x<y<z       abs((z-y) - (y-x))
    无法融掉的要加入数组中
    """
    while len(input_list) >= 3:
        input_list.sort(reverse=True)  # 将 input_list 从大到小排序
        x, y, z = input_list[2], input_list[1], input_list[0]
        input_list = input_list[3:]
        if x == y and y == z:
            continue
        elif x == y and y < z:
            input_list.append(z-y)
        elif x < y and y == z:
            input_list.append(y-x)
        elif x < y and y < z:
            input_list.append(abs((z-y)-(y-x)))

    if len(input_list) == 2 or len(input_list) == 1:
        return max(input_list)
    else:
        return 0


if __name__ == "__main__":
    n = int(input())
    input_list = list(map(int, input().split(" ")))

    print(solution(n, input_list))
