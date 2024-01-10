# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 89_gray_code
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/2/2 22:22
-------------------------------------------------
"""
import copy


class Solution:
    def __init__(self):
        self.res = []

    def grayCode(self, n):
        track = []
        self.back_track([0, 1], track, n)
        return self.res

    def back_track(self, choice_list, track, n):
        if len(track) == n:
            self.res.append(int("".join(copy.deepcopy(track)), 2))
            return
        """
        不可以使用这种方式，因为 "格雷编码" 的特点：上一个接的 0 1，同行的接 1 0
            —— 0
           /
          0 —— 1
         /
        0   
         \
          1 —— 1
           \
            —— 0

        xxxxxxxxxxxxxxxxxxx
        for i in choice_list:
            track.append(str(i))
            if i == 0:
                self.back_track([0, 1], track, n)
            else:
                self.back_track([1, 0], track, n)
            track.pop()
        xxxxxxxxxxxxxxxxxxx
        """

        track.append(str(choice_list[0]))
        self.back_track([0, 1], track, n)
        track.pop()

        track.append(str(choice_list[1]))
        self.back_track([1, 0], track, n)
        track.pop()


if __name__ == "__main__":
    s = Solution()
    s.grayCode(3)
