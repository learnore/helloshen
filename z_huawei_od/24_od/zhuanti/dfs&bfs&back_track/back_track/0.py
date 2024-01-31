# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 暴力穷举 回溯框架
  Description :


result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.append(路径)
        return

    for choice in 选择列表:
        1 排除选项

        2 做选择
        3 backtrack(路径, 选择列表)
        4 撤销选择


  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 18:04
-------------------------------------------------
"""
import copy


results = []
def solution(input_str, n):
    # base case
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
    """ 要求相同的字符不能相邻 """
    if len(path) == n:
        path = copy.deepcopy(path)                     # ***********
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

        # 开始进一步选择
        back_track(path, temp_str, n)

        # 撤销选择
        # input_str 不变 ，所以不用处理
        path.pop()


if __name__ == "__main__":
    print("chenyushen")
