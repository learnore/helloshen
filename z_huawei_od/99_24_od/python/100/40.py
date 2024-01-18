# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 40
  Description :

🎃样例1
输入
1,0,1
输出
2
说明:
1个小车占第1个车位，第二个车位空，1个小车占第3个车位，最少有两辆车



🎃样例2
输入
1,1,0,0,1,1,1,0,1
输出
3
说明:
1个货车占第1、2个车位，第3、4个车位空，1个卡车占第5、6、7个车位
第8个车位空，1个小车占第9个车位，最少3辆车


🎃样例3
输入
1,1,0,0,1,1,1,1,1,1,1,1,0,1
输出
4

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/18 14:57
-------------------------------------------------
"""


def solution(cars):
    """
    根据当前停车显示，猜测最少停了几辆车，思路：
    ①将一维数组变成字符串
    ②规则：111算卡车，算1辆，用字符3代替
           11 是货车，算1辆，用字符2代替
           1 是小车，算1辆，不变
    ③数一数，替换的字符串里面有多少个1、2、3就是几辆车
    """
    results = 0
    cars_str = "".join([str(i) for i in cars]).replace("111", "3").replace("11", "2")
    for i in cars_str:
        if i == "3" or i == "2" or i == "1":
            results += 1

    return results


if __name__ == "__main__":
    cars = list(map(int, input().split(",")))
    print(solution(cars))
