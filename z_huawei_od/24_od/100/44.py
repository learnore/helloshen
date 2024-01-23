# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 44
  Description :

🎃样例1
输入
4
100 200 300 500
1 2
1 3
2 4
输出
700
说明：
成员1,2, 3组成的小家庭财富值为600
成员2,4组成的小家庭财富值为700


🎃样例2
输入
4
100 200 300 500
1 2
1 3
1 4
输出
1100
说明：
成员1,2,3,4组成的小家庭财富值为1100

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/18 19:38
-------------------------------------------------
"""
from collections import defaultdict


def solution(n, wealths, nodes):
    """
    题目说是树，但是没说一个父结点有几个孩子
    小家庭的定义：父节点的财富 + 父结点直接连接的子结点的财富之和
    """
    max_wealth = 0

    tree = defaultdict(list)            # ****** 直接用 tree = [] 会在 tree[parent] 时报错
    for node in nodes:
        parent, child = node[0], node[1]
        tree[parent-1].append(child-1)

    for i in range(n):
        sum_wealth = wealths[i]
        for j in tree[i]:
            sum_wealth += wealths[j]
        max_wealth = max(max_wealth, sum_wealth)

    return max_wealth


if __name__ == "__main__":
    n = int(input())
    wealths = list(map(int, input().split(" ")))
    nodes = []
    for i in range(n-1):
        nodes.append(list(map(int, input().split(" "))))

    print(solution(n, wealths, nodes))
