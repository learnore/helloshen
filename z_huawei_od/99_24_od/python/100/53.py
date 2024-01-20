# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 53
  Description :

🎃样例1
输入
3 1 1 2
3 1 2 3
2
输出
4
说明：
用例中，需要取2对元素
取第一个数组第0个元素与第二个数组第0个元素组成1对元素[1,1];
取第一个数组第1个元素与第二个数组第0个元素组成1对元素[1,1];
求和为1+1+1+1=4，为满足要求的最小和。


🎃样例2
输入
4 1 1 2 3
3 1 2 3
3
输出
7

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 12:03
-------------------------------------------------
"""


def solution(input_list_1, input_list_2, k):
    """
    解题：第一个数组任意一个元素与第二个数组任意一个元素，都可以构成一对，共有 n*m 对
    找出 k 对，和最小的
    """
    # 暴力解
    sum_list = []
    for i in input_list_1:
        for j in input_list_2:
            sum_list.append(i+j)

    sum_list.sort(key=lambda x: x, reverse=False)
    result = 0
    for i in range(k):
        result += sum_list[i]

    return result


if __name__ == "__main__":
    input_list_1 = list(map(int, input().split(" ")))
    input_list_2 = list(map(int, input().split(" ")))
    k = int(input())

    print(solution(input_list_1, input_list_2, k))
