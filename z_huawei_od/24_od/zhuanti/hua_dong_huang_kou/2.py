# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 贪吃的猴子(100)
  Description :

🎃题目描述
一只贪吃的猴子，来到一个果园，发现许多串香蕉排成一行，每串香蕉上有若干根香蕉。
每串香蕉的根数由数组numbers给出。猴子获取香蕉，每次都只能从行的开头或者末尾获取，并且只能获取N次，求猴子最多能获取多少根香蕉.

🎃输入输出
输入
第一行为数组numbers的长度
第二行为数组numbers的值每个数字通过空格分开
第三行输入为N，表示获取的次数

输出
能获取的最大数值

🎃样例1
输入
7
1 2 2 7 3 6 1
3
输出
10


🎃样例2
输入
3
1 2 3
3
输出
6
说明
全部获取所有的香蕉，因此最终根数为1+2+3 = 6


🎃样例3
输入
4
4 2 2 3
2
输出
7
说明
第一次获取香蕉为行的开头，第二次获取为行的末尾，因此最终根数为4+3 =7

  Summary     : 1、本题的猴子，只能从首部或者尾部取数据，这一个条件限制
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 11:42
-------------------------------------------------
"""


def solution(n, numbers, m):
    """
    解题思路：
    1、反向思考，找出滑动窗口中的最少的香蕉数，剩下的就是最大的香蕉数量（因为猴子只能从数组的2边取值）
    2、滑动窗口的大小 = n - m(猴子可以取的个数)
    """
    windows_size = n-m
    windows_sum = sum(numbers[:windows_size])
    min_sum = windows_sum

    for i in range(windows_size, len(numbers)):
        windows_sum = windows_sum - numbers[i-windows_size] + numbers[i]
        min_sum = min(min_sum, windows_sum)

    return sum(numbers) - min_sum


if __name__ == "__main__":
    n = int(input())
    input_list = list(map(int, input().strip().split(" ")))
    m = int(input())
    print(solution(n, input_list, m))
