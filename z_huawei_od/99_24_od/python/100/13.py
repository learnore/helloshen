# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 13
  Description :
----------------- 用例 -------------
输入
10 10 56 34 99 1 87 8 99 3 255 6 99 5 255 4 99 7 255 2 99 9 255 21
3 4
输出
99

----------------- 用例 -------------
输入
10 10 255 34 0 1 255 8 0 3 255 6 0 5 255 4 0 7 255 2 0 9 255 21
3 4
输出
0

  Summary     : 1、根据数据，还原图像（也就是数组的值）
                2、取出数组中的值即可
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/8 16:25
-------------------------------------------------
"""


def restore_image(compressed_data):
    # 解析行数、列数
    m, n = compressed_data[0], compressed_data[1]
    compressed_data = compressed_data[2:]
    new_compressed_data = []
    for i in range(0, len(compressed_data), 2):
        for j in range(compressed_data[i + 1]):
            new_compressed_data += [compressed_data[i]]

    # 解析压缩数据
    results = []
    count = 0
    for i in range(m):
        temp_res = []
        for j in range(n):
            temp_res += [new_compressed_data[count]]
            count += 1

        results.append(temp_res)

    return results


if __name__ == "__main__":
    compressed_data = list(map(int, input().split()))
    x, y = map(int, input().split())

    results = restore_image(compressed_data)        # 获取指定像素的灰阶值
    print(results[x][y])
