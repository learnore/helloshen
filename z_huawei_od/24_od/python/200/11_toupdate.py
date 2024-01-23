# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 11
  Description : 待优化代码逻辑 todo

🎃题目描述
算法工程师小明面对着这样一个问题， 需要将通信用的信道分配给尽量多的用户：
信道的条件及分配规则如下：

1、所有信道都有属性：“阶”，阶为r的信道的容量为2^r比特；
2、所有用户需要传输的数据量都一样：D比特；
3、一个用户可以分配多个信道，但每个信道只能分配给一个用户；
4、只有当分配给一个用户的所有信道的容量和>=D，用户才能传输数据；

给出一组信道资源，最多可以为多少用户传输数据?

🎃输入输出
输入
第一行，一个数字R，R为最大阶数，0<=R<20
第二行，R+1个数字，用空格隔开；代表每种信道的数量Ni，按照阶的值从小到大排列0<=i<=R，0<=Ni<1000.
第三行，一个数字D，D为单个用户需要传输的数据量，0<D<1000000

输出
一个数字，代表最多可以供多少用户传输数据

🎃样例1
输入
5
10 5 0 1 3 2
30
输出
4


🎃样例2
输入
5
0 0 0 0 3 2
24
输出
3


  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/22 15:21
-------------------------------------------------
"""
from collections import defaultdict


def solution(n, channels, channel_sum, client_datas):
    """
    解题思路：
    1、最大最符合的信道先分配
    2、当刚好分配超过时，则选择更低的信道分配，比如 30 = 16 + 8 + 4 + 2 = 16 + 8 + 2 + 2 + 2（若没有4信道）
    """
    results = 0
    while channel_sum > client_datas:

        temp_data = client_datas
        for i in range(n, -1, -1):
            if channels[2**i] and 2 ** i >= temp_data:       # 如果有，且 一条信道就能传用户数据
                results += channels[2 ** i]
                channel_sum -= channels[2**i] * (2**i)            # 调整消耗
                channels[2 ** i] = 0
                continue

            # 一条信道不能直接覆盖整个数据的
            if channels[2**i]:
                x, y = temp_data // (2**i), temp_data % (2**i)        # x 指消耗 2**n 信道的个数， y 指剩余的用户数据

                if x > channels[2 ** i]:                        # 不够传，矫正信息
                    y += (x - channels[2 ** i]) * (2 ** i)      # 剩余的用户数据
                    x = channels[2 ** i]

                    channels[2 ** i] = 0                        # 归0

                else:
                    channels[2 ** i] -= x                       # 消耗 x 个

                channel_sum -= x * (2 ** i)
                temp_data -= x * (2 ** i)

                if temp_data <= 0:
                    results += 1
                    break

        if temp_data:       # 全用最小的满足的信道分配
            for i in range(0, n+1):
                if channels[2**i]:
                    pass        # todo

    return results


if __name__ == "__main__":
    n = int(input())
    input_channels = list(map(int, input().strip().split(" ")))
    channel_sum = 0
    for i in range(len(input_channels)):
        channel_sum += 2**i * input_channels[i]

    channels = defaultdict(list)
    for i in range(n+1):
        channels[2**i] = input_channels[i]
    client_datas = int(input())

    print(solution(n, channels, channel_sum, client_datas))

