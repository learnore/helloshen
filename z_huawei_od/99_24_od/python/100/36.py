# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 36
  Description :

🎃样例1
输入
1,3,3,3,2,4,4,4,5
输出
3,4,1,2,5


🎃样例2
输入
1,4,4,4,2,3,3,3,5
输出
4,3,1,2,5

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 19:58
-------------------------------------------------
"""
from collections import Counter


def solution(input_list):
    """ 统计数组元素，从多到少排序，相同则按照原来得相对位置排序 """
    result = []
    counter = Counter(input_list)
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    for c in counter:
        key, value = c[0], c[1]
        result.append(key)

    return result


if __name__ == "__main__":
    input_list = list(map(int, input().split(",")))
    print(",".join([str(i) for i in solution(input_list)]))
