# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 21
  Description : 简单逻辑判断 + Counter类的使用(做字典用)

🎃样例1
输入
2
present
present present
输出
true
true
1
2
3
4
5
6
7

🎃样例2
输入
2
present
present absent present present leaveearly present absent
输出
true
false
1
2
3
4
5
6
7

🎃样例3
输入
1
present absent absent
输出
false

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/9 22:25
-------------------------------------------------
"""
from collections import Counter


def can_get_award(input_datas):
    count = Counter(input_datas)

    # 任意连续7次考勤，缺勤、迟到、早退超过3次
    if len(input_datas) > 7:
        for i in range(0, len(input_datas) - 7):
            new_count = Counter(input_datas[i:i+7])
            if new_count["absent"] + new_count["late"] + new_count["leaveearly"] > 3:
                return False
    else:
        if count["absent"] + count["late"] + count["leaveearly"] > 3:
            return False

    # 缺勤超过一次就没有全勤
    if count["absent"] > 1:
        return False

    # 连续的迟到、早退时，则没有全勤
    late_leaveearly = 0
    for item in range(len(input_datas)):
        if item == "late" or item == "leaveearly":
            late_leaveearly += 1
            if late_leaveearly == 2:
                return False
        else:
            late_leaveearly = 0

    return True


if __name__ == "__main__":
    N = int(input())

    check_list = []
    for i in range(N):
        input_datas = list(map(str, input().split(" ")))
        check_list.append(input_datas)

    for item in check_list:
        print(can_get_award(item))
