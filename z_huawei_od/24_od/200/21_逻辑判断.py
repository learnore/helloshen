# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 21
  Description :

🎃题目描述
孙悟空喜欢吃蟠桃，一天他乘守卫蟠桃园的天兵天将离开了而偷偷的来到王母娘娘的蟠桃园偷吃蟠桃。

已知蟠桃园有 N 棵蟠桃树，第 i 棵蟠桃树上有 N[i]（大于 0）个蟠桃，天兵天将将在 H（不小于蟠桃树棵数）小时后回来。

孙悟空可以决定他吃蟠桃的速度 K（单位：个/小时），每个小时他会选择一颗蟠桃树，从中吃掉 K 个蟠桃，如果这棵树上的蟠桃数小于 K，他将吃掉这棵树上所有蟠桃，然后这一小时内不再吃其余蟠桃树上的蟠桃。

孙悟空喜欢慢慢吃，但仍想在天兵天将回来前将所有蟠桃吃完。

求孙悟空可以在 H 小时内吃掉所有蟠桃的最小速度 K（K 为整数）。

🎃输入输出
输入
第一行输入为 N 个数字，N 表示桃树的数量，这 N 个数字表示每颗桃树上蟠桃的数量。
第二行输入为一个数字，表示守卫离开的时间 H

输出
吃掉所有蟠桃的 最小速度 K（K 为整数）或 输入异常时输出0

🎃样例1
输入
3 11 6 7
8
输出
4
说明：
天兵天将8个小时后回来，孙悟空吃掉所有蟠桃的最小速度4。
第1小时全部吃完第一棵树，吃3个，
第2小时吃4个，第二棵树剩7个，
第3小时吃4个，第二棵树剩3个，
第4小时吃3个，第二棵树吃完，
第5小时吃4个，第三棵树剩2个，
第6小时吃2个，第三棵树吃完，
第7小时吃4个，第4棵树剩3个，
第8小时吃3个，第4棵树吃完。


🎃样例2
输入
2 3 4 5
4
输出
5


🎃样例3
输入
2 3 4 5
3
输出
0


🎃样例4
输入
30 11 23 4 20
6
输出
23

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 20:17
-------------------------------------------------
"""
import math


def solution(input_list, h):
    """
    1、每小时选一颗桃子树，从树上吃掉 result个
    2、吃掉一棵树的桃子后，剩余时间不再吃其他树上的桃
    3、result 尽可能小，且要再守卫回来前吃完所有桃子

    """
    # 肯定吃不完
    if h <= 0 or not input_list or len(input_list) > h:
        return 0

    # 刚好吃完
    if len(input_list) == h:
        return max(input_list)

    # 不仅能吃完，还可以慢慢吃
    result = 0
    for i in range(1, max(input_list)):
        temp_h = h
        for t in input_list:
            if t <= i:  # 刚好吃完
                temp_h -= 1
            elif t > i:
                temp_h -= math.ceil(t/i)

        if temp_h >= 0:
            result = i
            break

    return result


if __name__ == "__main__":
    input_list = list(map(int, input().strip().split(" ")))
    h = int(input())
    print(solution(input_list, h))
