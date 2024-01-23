# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 10
  Description :

用例1
输入
[[1,4],[2,5],[7,9],[14,15]]
输出
[[1,5],[7,9],[14,15]]

  Summary     : 1、操作数据前，先排序，会方便很多
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/22 15:03
-------------------------------------------------
"""


def solution(times):
    """
    解题方法：
    1、将所有时间段的开始时间，按照从小到大排序
    2、开始循环，若当前循环的开始时间小于前一个的结束时间，那就合并当前时间段和前一个时间段
    """
    times.sort(key=lambda x: x[0], reverse=False)
    results = []
    for t in times:
        if not results or t[0] > results[-1][1]:        # 如果 results 还没有时间段 或者 当前时间段的开始时间不在上一个时间段中，那就将当前时间段加入
            results.append(t)

        else:       # 与上一个时间段合并
            results[-1][1] = max(results[-1][1], t[1])      # 取当前时间段和上一个时间段的最大的一个值

    return results


if __name__ == "__main__":
    input_list = eval(input().strip())
    results = solution(input_list)
    print(str(results).replace(" ", ""))
