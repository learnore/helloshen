# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 5
  Description :

-------- 示例 --------
输入
1
0 1 2 3 4
输出
0-2

-------- 示例 --------
输入
1
0 1 2 0 1 2
输出
0-5

-------- 示例 --------
输入
1
0 1 2 5 0 1 2
输出
0-2 4-6

-------- 示例 --------
输入
2
0 0 100 2 2 99 0 2
输出
0-1 3-4 6-7

-------- 示例 --------
输入
3
0 7 8 99 20 1
NULL

-------- 示例 --------
输入
1
10 1 1 3 4
输出
1-2

  Author      : chenyushencc@gmail.com
  date        : 2024/1/4 20:59
-------------------------------------------------
"""


# TODO 听说还可以用 dfs - ChatGPT


def find_longest_time_period(min_average_lost, failure_rates):
    """
    # 暴力解
    """
    temp_res = []
    for i in range(len(failure_rates)):
        total = 0
        for j in range(i, len(failure_rates)):
            total += failure_rates[j]
            average_lost = total / (j-i+1)
            if average_lost <= min_average_lost:
                temp_res.append((i, j, j-i+1))      # 记录：    起点-终点-差值
            else:
                break

    temp_res.sort(key=lambda x: (x[2]), reverse=True)      # reverse=True 差值越大越在前面

    _, _, max_differ = temp_res[0]              # 注意元组的取值方式
    if not temp_res or max_differ == 1:
        return ["NULL"]

    results = []
    for item in temp_res:
        _, _, differ = item
        if differ == max_differ:
            results.append(f"{item[0]}-{item[1]}")      # √√√

    return results


if __name__ == "__main__":
    min_average_lost = int(input())
    failure_rates = list(map(int, input().split()))

    results = find_longest_time_period(min_average_lost, failure_rates)
    for item in results:
        print(item, end=" ")        # √√√




