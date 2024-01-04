# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 4
  Description :

-------- 示例1 --------
输入
5 4
1
1
2
3
5
1 2 3
1 4
3 4 5
2 3 4
输出
3
4
1
2

-------- 示例2 --------
输入
3 3
2
1
3
1 2 3
2 3
1 2
输出
1
2
3

  Author      : chenyushencc@gmail.com
  date        : 2024/1/4 19:21
-------------------------------------------------
"""


def solution(N, M, texing_list, yongli_list):
    results = [(i+1, sum(texing_list[id-1] for id in case)) for i, case in enumerate(yongli_list)]

    results.sort(key=lambda x: (x[1]), reverse=True)

    # results = [(item[0], item[1]) for item in results]        # 用于检查
    results = [item[0] for item in results]
    return results


if __name__ == "__main__":
    # 输入特性数量和测试用例数量
    len_A, len_B = map(int, input().split())

    # 输入特性优先级
    texing_list = [int(input()) for _ in range(len_A)]

    # 输入测试用例关联的特性ID列表
    yongli_list = [list(map(int, input().split())) for _ in range(len_B)]

    # 调用方法
    results = solution(len_A, len_B, texing_list, yongli_list)

    # 输出
    for r in results:
        print(r)


