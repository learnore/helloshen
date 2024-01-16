# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 27
  Description :

🎃样例1
输入
10
1 2 1 2 1 2 1 2 1 2
5
输出
2
1
2

🎃样例2
输入
5
1 2 3 4 5
3
输出
0

🎃样例3
输入
12
1 1 1 2 2 2 3 3 3 4 4 4
3
输出
4
1
2
3
4

🎃样例4
输入
13
1 1 1 4 4 4 4 2 2 2 3 3 3
3
输出
4
4
1
2
3

  Summary     : counter = sorted(counter.item(), key=lambda x: (x[1], -x[0]), reverse=True )
                    1、counter.item() 作为字典使用
                    2、key=lambda 容易忘记 key= 参数
                    3、(x[1], -x[0]), reverse=True 表示用 value 从大到小，相同时，用 key 从小到大
                    4、最终的 counter 从字典类型{ : }，变成元组类型( , )，所以 for 循环的时候，不用再使用 counter.item()
                    5、for 循环的元组，还是 (key, value) 的格式，并没有因为 (x[1], -x[0]) 而改变顺序

  Author      : chenyushencc@gmail.com
  date        : 2024/1/15 15:26
-------------------------------------------------
"""
from collections import Counter


def solution(n, input_list, x_value):
    """ 统计 input_list 中每个数字的个数，输出超过 x_value 的个数和排序顺序 """
    all_num, results = 0, []
    counter = Counter(input_list)

    # 此时经过排序后变成元组，但还是 (key, value)
    counter = sorted(counter.items(), key=lambda x: (x[1], -x[0]), reverse=True)
    for c in counter:
        key, value = c[0], c[1]
        if value >= x_value:
            all_num += 1
            results.append(key)
    return all_num, results


if __name__ == "__main__":
    n = int(input())
    input_list = list(map(int, input().split()))
    x_value = int(input())

    all_num, results,  = solution(n, input_list, x_value)
    print(all_num)
    for i in results:
        print(i)

