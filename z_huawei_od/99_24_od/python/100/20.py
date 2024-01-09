# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 20
  Description :

🎃样例1
输入
4
8 6 2 8 6
camila 66 70 46 158 80
victoria 94 76 86 189 211
anthony 29 17 83 21 48
emily 53 97 1 19 218
输出
victoria
camila
emily
anthony

🎃样例2
输入
5
5 6 6 1 2
camila 13 88 46 26 169
grace 64 38 87 23 103
lucas 91 79 98 154 79
leo 29 27 36 43 178
ava 29 27 36 43 178
输出
lucas
grace
camila
ava
leo

  Summary     : 1、热度值相等的，先变小写，再排序
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/9 20:27
-------------------------------------------------
"""


def calculate_heat(watch, star, fork, issue, mr,
                   watch_project, star_project, fork_project, issue_project, mr_project):

    return watch*watch_project + star*star_project + fork*fork_project + issue*issue_project + mr*mr_project


if __name__ == "__main__":
    N = int(input())
    watch, star, fork, issue, mr = map(int, input().split(" "))

    results = []
    for i in range(N):
        project = list(map(str, input().split()))
        sum_score = calculate_heat(watch, star, fork, issue, mr,
                                   int(project[1]), int(project[2]), int(project[3]),
                                   int(project[4]), int(project[5]))
        results.append((project[0], sum_score))

    """
    小技巧： 
    x[1]要从大到小排序
    x[0].lower() 又要从小到大排序
    则将 x[1] 添上负号，然后统一从小到大排序即可
    """
    results.sort(key=lambda x: (-x[1], x[0].lower()), reverse=False)
    for i in results:
        print(i[0])
