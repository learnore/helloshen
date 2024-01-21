# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 51
  Description :

用例
输入
10001
输出
1

用例
输入
1001000100001
输出
2


  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 10:29
-------------------------------------------------
"""


def solution(input_str):
    """
    解决方案：000 替换为2，表示010中间可以落座1个人
    00 不可落座                1 2 0
    000     0000    可落座1人  3 4 1
    00000   000000  可落座2人  5 6 2
    0000000 00000000 可落座3人 7 8 3
    """
    temp_list = []      # 存储每个间隔0的个数
    count = 0
    for i in input_str:
        if i == "0":
            count += 1
        elif count != 0:
            temp_list.append(count)
            count = 0

    result = 0
    for i in temp_list:
        if i == 1 or i == 2:
            continue

        if i % 2 == 0:      # 偶数
            result += (i // 2 - 1)
        else:
            result += (i-1)//2

    return result


if __name__ == "__main__":
    input_str = input().strip()
    print(solution(input_str))
