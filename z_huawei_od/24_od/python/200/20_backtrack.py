# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 20 字符串拼接
  Description :

🎃题目描述
给定 M（0 < M ≤ 30）个字符（a-z），从中取出任意字符（每个字符只能用一次）拼接成长度为 N（0 < N ≤ 5）的字符串

要求相同的字符不能相邻，计算出给定的字符列表能拼接出多少种满足条件的字符串，

输入非法或者无法拼接出满足条件的字符串则返回0。

🎃输入输出
输入
给定的字符列表和结果字符串长度，中间使用空格(" ")拼接

输出
满足条件的字符串个数

🎃样例1
输入
abc 1
输出
3
说明：
给定的字符为a,b,c，结果字符串长度为1，可以拼接成a,b,c，共3种
1


🎃样例2
输入
dde 2
输出
2
说明：
给定的字符为dde，结果字符串长度为2，可以拼接成de,ed，共2种
1


🎃样例3
输入
abc 2
输出
6
说明：
构成ab ac ba bc ca cb
1


🎃样例4
输入
aab 2
输出
2
说明：
只能构成ab,ba


🎃样例5
输入
aabc 2
输出
6


🎃样例6
输入
aabb 4
输出
2


🎃样例7
输入
aab 3
输出
1


🎃样例8
输入
abcd 2
输出
12


🎃样例9
输入
abcd 4
输出
24


🎃样例10
输入
abc 4
输出
0


🎃样例11
输入
a 2
输出
0


🎃样例12
输入
a 1
输出
1


🎃样例13
输入
aaabbb 3
输出
2


🎃样例14
输入
abcdef 3
输出
120

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 17:56
-------------------------------------------------
"""
import copy


results = []
def solution(input_str, n):
    """
    解题思路：
    1、
    """
    if n == 1:
        return len(input_str)
    if len(input_str) <= 0 or len(input_str) > 30 or n <= 0 or n > 5:
        return 0
    if len(input_str) < n:
        return 0
    # if len(input_str) == n:       # aabb 4 应该返回结果2 a b a b 或 b a b a
    #     return 1

    back_track([], input_str, n)

    result = set(tuple(i) for i in results)
    result = [list(i) for i in result]

    return len(result)


def back_track(path, input_str, n):
    """
    要求相同的字符不能相邻
    解题思路：
    1、
    """
    if len(path) == n:
        path = copy.deepcopy(path)
        results.append(path)
        return

    for i in range(len(input_str)):
        if len(path) and path[-1] == input_str[i]:     # 相同的字符不可以放在一起
            continue

        # 做选择
        path.append(input_str[i])
        if i == 0:
            temp_str = input_str[1:]
        else:
            temp_str = input_str[:i] + input_str[i + 1:]

        back_track(path, temp_str, n)

        # 撤销选择
        # input_str 不变
        path.pop()


if __name__ == "__main__":
    input_str, n = list(map(str, input().strip().split(" ")))
    n = int(n)

    print(solution(input_str, n))
