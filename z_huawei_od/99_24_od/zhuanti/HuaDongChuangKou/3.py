# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 最差产品奖(200)
  Description :

🎃题目描述
A公司准备对他下面的N个产品评选最差奖，评选的方式是首先对每个产品进行评分，然后根据评分区间计算相邻几个产品中最差的产品。

评选的标准是依次找到从当前产品开始前M个产品中最差的产品，请给出最差产品的评分序列。

🎃输入输出
输入
第一行，数字M，表示评分区间的长度，取值范围是0<M<10000
第二行，产品的评分序列，比如[12,3,8,6,5]， 产品数量N范围是-10000 < N <10000

输出描述
评分区间内最差产品的评分序列

🎃样例1
输入
3
12,3,8,6,5
输出
3,3,5
说明：
12,3，8 最差的是3
3,8，6 最差的是3
8,6，5 最差的是5


🎃样例2
输入
3
1,2,3,4,5,6,7
输出
1,2,3,4,5

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 11:59
-------------------------------------------------
"""


def solution(m, input_list):
    """
    解题思路
    1、在窗口中选择最小的输出
    """
    results = []

    for i in range(m, len(input_list)+1):
        results.append(min(input_list[i-m: i]))

    return results


if __name__ == "__main__":
    m = int(input())
    input_list = list(map(int, input().strip().split(",")))
    print(",".join([str(i) for i in solution(m, input_list)]))
