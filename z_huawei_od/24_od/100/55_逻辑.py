# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 55
  Description :

🎃样例1
输入
7
8
4
6
3
1
6
7
10
输出
3
说明
gems = [8,4,6,3,1,6,7], value = 10
最多购买的宝石为gems[2]至gems[4]或者gems[3]至gems[5]


🎃样例2
输入
0
1
输出
0


🎃样例3
输入
9
6
1
3
1
8
9
3
2
4
15
输出
4


🎃样例4
输入
9
1
1
1
1
1
1
1
1
1
10
输出
9

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 14:25
-------------------------------------------------
"""


def solution(n, gems, value):
    """ 返回可以购买连续的宝石最大数量 """
    result = 0
    for i in range(len(gems)):
        temp_value = 0
        temp_res = 0

        while temp_value < value and i < len(gems):
            temp_value += gems[i]
            temp_res += 1
            i += 1

        if temp_value > value:        # 则最后一次不能加入，买不了，钱不够
            temp_res -= 1

        result = max(result, temp_res)

    return result


if __name__ == "__main__":
    n = int(input())
    gems = []
    for i in range(n):
        gems.append(int(input()))
    value = int(input())
    print(solution(n, gems, value))
