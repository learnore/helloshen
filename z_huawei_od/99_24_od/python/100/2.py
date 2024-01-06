# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 2
  Description : 参考：https://www.nowcoder.com/discuss/567360638045925376?sourceSSR=search

-------- 示例1 --------
输入:
2 2
1 1
2 2
输出
1 2

-------- 示例2 --------
输入:
2 2
1 2
2 3
输出
1 2

-------- 示例3 --------
输入:
1 2
2
1 3
输出
2 3

-------- 示例4 --------
输入:
3 2
1 2 5
2 4
输出:
5 4

  Author      : chenyushencc@gmail.com
  date        : 2024/1/2 13:29
-------------------------------------------------
"""


def find_minimum_swap(A, B):
    A.sort()        # 题目要求A中最小的进行交换，将list数据排序

    total_difference = sum(A) - sum(B)      # 计算2个CPU合力之差

    b_set = set(B)          # 将 list(B) set化
    for a_cpu in A:
        target_b_cpu = a_cpu - (total_difference // 2)
        if target_b_cpu in b_set:
            return a_cpu, target_b_cpu

    """
    # 等式： (a_cpu - b_cpu) *2 = total_difference
    # 从A中取一个数，从B中取一个数，2数只差的2备，是sum之差，则就选这两个
    """


if __name__ == "__main__":
    # 输入
    L1, L2 = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 输出
    result = find_minimum_swap(A, B)
    print(result[0], result[1])
    