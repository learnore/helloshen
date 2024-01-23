# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : dfs - 回溯

🎃题目描述
小杨申请了一个保密柜，但是他忘记了密码。只记得密码都是数字，且所有数字都是不重复的。

请你根据他记住的数字范围和密码的最小数字数量，帮他算下有哪些可能的组合，规则如下：
1、输出的组合都是从可选的数字范围中选取的，不能重复；

2、输出的密码数字要按照从小到大的顺序排列，密码组合需要按照字母顺序，从小到大的顺序排序。

3、输出的每一个组合的数字的数量要大于等于密码最小数字数量；

4、如果可能的组合为空，则返回 “None”

🎃输入输出
输入
1、输入的第一行是可能的密码数字列表，数字间以半角逗号分隔
2、输入的第二行是密码最小数字数量

输出
可能的密码组合，每种组合显示成一行，每个组合内部的数字以半角逗号分隔，从小到大的顺序排列。
输出的组合间需要按照字典序排序。
比如：2,3 ,4放到2 ,4的前面

🎃样例1
输入
2,3,4
2
输出：
2,3
2,3,4
2,4
3,4
说明：
最小密码数最是两个,可能有三种组合:
2,3
2,4
3,4
三个密码有一种:2,3,4

🎃样例2
输入
1,2,3,4,5
3
输出
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,5
1,2,4
1,2,4,5
1,2,5
1,3,4
1,3,4,5
1,3,5
1,4,5
2,3,4
2,3,4,5
2,3,5
2,4,5
3,4,5

  Description : 
  Summary     : 1、回溯 = dfs
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 16:31
-------------------------------------------------
"""
import copy


def backtrack(n, path, choice):
    """
    回溯 - 穷举
    """
    if len(path) >= n:
        path = copy.deepcopy(path)
        results.append(path)
        # 这里不用return，因为只要是满足 len(path) >= n 都可以加入
        # 加了 return 就只返回 len(path) == n 的数组了

    for i in choice:        # 继续在选择列表中选择一个
        if i in path or (len(path) and i < max(path)):       # 排除已经选择的 且 只要逐步增长的
            continue

        path.append(i)      # 做选择
        backtrack(n, path, choice)
        path.remove(i)      # 撤销选择


if __name__ == "__main__":
    input_list = list(map(int, input().split(",")))
    n = int(input())
    input_list.sort(key=lambda x: x, reverse=False)

    results = []
    backtrack(n, [], input_list)
    for i in results:
        print(",".join([str(j) for j in i]))

