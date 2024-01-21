# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 46_permutations
  Description : 46. 全排列
  Author      : chenyushencc@gmail.com
  date        : 2023/2/2 16:46
-------------------------------------------------
"""
import copy


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        track = []  # 路径
        self.back_track(nums, track)
        return self.res

    def back_track(self, nums, track):
        # base case
        if len(nums) == len(track):
            self.res.append(copy.deepcopy(track))       # TODO 思考：为什么不用 self.res.append(track) ？？
            return

        for i in range(len(nums)):
            if nums[i] in track:
                continue

            track.append(nums[i])
            self.back_track(nums, track)
            # print(track)
            track.pop()


if __name__ == "__main__":
    s = Solution()
    s.permute([1, 2, 3])
