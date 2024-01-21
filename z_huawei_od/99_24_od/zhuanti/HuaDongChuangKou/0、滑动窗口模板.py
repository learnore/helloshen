# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 8、滑动窗口模板
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/20 20:47
-------------------------------------------------
"""

from collections import defaultdict, Counter


def sliding_window(s, t):
    needs = Counter(t)
    window = defaultdict(int)

    left, right, valid = 0, 0, 0

    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 右移窗口
        right += 1
        # 进行窗口内数据的一系列更新
        # ...

        # debug 输出的位置
        print(f"window: [{left}, {right}]")

        # 判断左侧窗口是否要收缩
        while window or needs:      # shrink
            # d 是将移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1
            # 进行窗口内数据的一系列更新
            # ...


if __name__ == "__main__":
    # 示例用法
    sliding_window("ADOBECODEBANC", "ABC")
