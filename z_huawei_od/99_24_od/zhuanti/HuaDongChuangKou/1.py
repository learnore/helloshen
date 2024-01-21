# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1
  Description : 65、高矮个子排队(100)

🎃题目描述
现在有一队小朋友，他们高矮不同，我们以正整数数组表示这一队小朋友的身高，如数组{5,3,1,2,3}。

我们现在希望小朋友排队，以"高" “矮” “高” “矮” 顺序排列，每一个高位置的小朋友要比相邻的位置高或者相等；每个 “矮” 位置的小朋友要比相邻的位置矮或者相等;

要求小朋友们移动的距离和最小，第一个从“高"位开始排，输出最小移动距离即可。

例如，在示范小队{5,3,1,2,3}中， {5, 1, 3, 2, 3}是排序结果。

{5,2,3, 1, 3}虽然也满足"高" “矮” “高” "矮"顺序排列，但小朋友们的移动距离大，所以不是最优结果。

移动距离的定义如下所示：

第二位小朋友移到第三位小朋友后面，移动距离为1，若移动到第四位小朋友后面，移动距离为2；

🎃输入输出
输入
排序前的小朋友，以英文空格的正整数：4 3 5 7 8
注：小朋友<100个

输出
排序后的小朋友，以英文空格分割的正整数: 4 3 7 5 8
备：4(高)3(矮)7(高)5(矮)8(高)，输出结果为最小移动距离，只有5和7交换了位置，移动距离都是1。

🎃样例1
输入
4 1 3 5 2
输出
4 1 5 2 3


🎃样例2
输入
1 1 1 1 1
输出
1 1 1 1 1
说明：
相邻位置可以相等

  Summary     : 1、按照滑动窗口的理解就是 高矮高 或 矮高矮
                2、本题解法可不用滑动窗口
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 11:25
-------------------------------------------------
"""


def solution(input_list):
    """
    解题思路：
    1、第一个是高个子
    """
    results = []
    for i in range(len(input_list)):
        # 偶数位置，不是最后一个元素，当前位置元素小于下一个位置元素
        if i % 2 == 0 and i < len(input_list)-1 and input_list[i] < input_list[i+1]:
            input_list[i], input_list[i + 1] = input_list[i+1], input_list[i]

        # 奇 不是最后一个元素  当前位置元素 大于  下一个位置元素
        elif i % 2 == 1 and i < len(input_list)-1 and input_list[i] > input_list[i+1]:
            input_list[i], input_list[i + 1] = input_list[i+1], input_list[i]

        results.append(input_list[i])

    return results


if __name__ == "__main__":
    input_list = list(map(int, input().strip().split(" ")))
    print(" ".join([str(i) for i in solution(input_list)]))
