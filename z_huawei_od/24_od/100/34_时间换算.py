# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 34
  Description :


🎃样例1
输入
2
App1 1 09:00 10:00
App2 2 11:00 11:30
09:30
输出
App1


🎃样例2
输入
2
App1 1 09:00 10:00
App3 2 09:00 10:00
09:30
输出
App3


🎃样例3
输入
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:20
输出
App2
说明
App1和App2的时段有冲突，App2优先级高，注册App2之后，App1自动注销，因此输出App2


🎃样例4
输入
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:50
输出
NA
说明：
App2优先级高会被注册, 然后App1被注销, App1被注销后, 09:50时刻没有应用注册，因此输出NA


🎃样例5
输入
1
App1 1 09:00 10:00
09:30
输出
App1


  Summary     : 1、用例保证在 00:00 - 24:00，且格式正确
                2、将 hh:mm 转换成分钟，方便比较时间大小
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 15:35
-------------------------------------------------
"""


def solution(input_lists, cur_minutes):
    """
    前提：
        删除重叠的优先级低的 app
        优先级相等的，则无法插入，遵循题中的先来后到原则

    ChatGPTf 给出的思路：
        将满足要求的所有 app 的名称和优先级，用元组格式，加入一个数组中
        输出优先级最大的即可

    返回当前时间点能使用的 app 名称，没有则返回 "NA"
    """
    # 第一步 删除重叠的优先级低的 app
    todel = []
    for i in range(len(input_lists)):
        if i in todel:      # 如果该位置要删除，则不操作
            continue

        name_i, priority_i, start_time_i, end_time_i = input_lists[i]
        for j in range(i+1, len(input_lists)):
            if j in todel:  # 如果该位置要删除，则不操作
                continue

            name_j, priority_j, start_time_j, end_time_j = input_lists[j]

            if end_time_i < start_time_j or end_time_j < start_time_i:      # 重叠情况比较复杂，直接考虑未重叠情况
                continue            # 没重叠
            else:                   # 重叠了
                if priority_i < priority_j:     # 重叠了，删除优先级低的
                    todel.append(i)
                else:                           # 优先级相同时遵循先来后到原则，删除后面的 j
                    todel.append(j)

    # 第二步 从大到小排序，先删除大的
    todel.sort(reverse=True)
    for i in todel:
        input_lists.pop(i)

    # 第三步 准备输出
    available_apps = []

    for app in input_lists:
        name, priority, start_minutes, end_minutes = app

        if start_minutes <= cur_minutes <= end_minutes:
            available_apps.append((name, int(priority)))

    if available_apps:
        available_apps.sort(key=lambda x: x[1], reverse=True)       # 从大到小排序
        return available_apps[0][0]
    else:
        return "NA"


def hhmm_mm(hhmm):
    """ 将时间 hh:mm 变成分钟 """
    h, m = map(int, hhmm.split(":"))
    return h*60 + m


if __name__ == "__main__":
    n = int(input())

    input_lists = []
    for i in range(n):
        name, priority, start_time, end_time = map(str, input().split(" "))
        start_time, end_time = hhmm_mm(start_time), hhmm_mm(end_time)       # 将开始时间和结束时间转换成分钟，方便比较
        input_lists.append((name, priority, start_time, end_time))

    cur_minutes = hhmm_mm(input())

    print(solution(input_lists, cur_minutes))

