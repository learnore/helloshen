# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 28
  Description :

🎃样例1
输入
[0,1,4,3,1,0,0,1,2,3,1,2,1,0]
输出
3
说明:
山峰所在的索引分别为 2,10,12

  Summary     : 1、只管 _1^1_ 的情况，不考虑 _1^^^^^1_ 连着的情况？？？？
                2、考虑前面2个位置和最后2个位置，可能出现山峰
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/16 19:00
-------------------------------------------------
"""


def solution(high_list):
    """ 返回山峰的个数 """
    result = 0

    for i in range(1, len(high_list)-1):
        # 判断规则：3个为一组，中间的比旁边的都大，则是山峰
        if high_list[i-1] < high_list[i] < high_list[i+1]:
            result += 1
        elif i == 1 and high_list[0] > high_list[1]:
            result += 1
        elif i == len(high_list)-2 and high_list[i] < high_list[i+1]:
            result += 1

    return result


if __name__ == "__main__":
    high_list = list(map(int, input().replace("[", "").replace("]", "").split(",")))
    result = solution(high_list)
    print(result)
