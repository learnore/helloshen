# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 63
  Description :

🎃样例1
输入
3 15 6 14
输出
3 21 9 17
说明
- 第1盘寿司的价格是3，没有比它价格更低的寿司，所以总价格就是它自己的价格，即3
- 第2盘寿司的价格是15，离它最近的价格更低的寿司是第3盘（价格6），所以总价格是15+6=21
- 第3盘寿司的价格是6，离它最近的价格更低的寿司是第1盘（价格3），所以总价格是6+3=9
- 第4盘寿司的价格是14，离它最近的价格更低的寿司是第1盘（价格3），所以总价格就是14+3=17


🎃样例2
输入
3 10 5 7
输出
3 15 8 10

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/20 12:52
-------------------------------------------------
"""


def solution(input_list):
    """
    解题思路：
    1、循环数组找下一个比当前值小的寿司
    2、只送一盘寿司
    3、找到 min，如果当前值是min那就不找了，没得送
    """
    min_value = min(input_list)
    result = []

    for i in range(len(input_list)):
        cur_value = input_list[i]
        if cur_value == min_value:
            result.append(cur_value)
            continue

        while True:
            i += 1
            if cur_value > input_list[(i+len(input_list))%len(input_list)]:
                cur_value += input_list[(i+len(input_list))%len(input_list)]
                break       # 找到了就撤

        result.append(cur_value)

    return result


if __name__ == "__main__":
    input_list = list(map(int, input().strip().split(" ")))
    print(" ".join([str(i) for i in solution(input_list)]))
