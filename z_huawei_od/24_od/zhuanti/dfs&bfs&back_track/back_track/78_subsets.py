# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 78_subsets
  Description : 78. 子集
  Author      : chenyushencc@gmail.com
  date        : 2023/2/2 16:04
-------------------------------------------------
"""
import copy


class Solution:
    def subsets(self, nums):
        res = [[]]
        for item in nums:
            res = res + [[item] + i for i in res]

        return res


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums):
        track = []
        self.back_track(nums, 0, track)
        return self.res

    def back_track(self, nums, start, track):
        self.res.append(copy.deepcopy(track))  # copy.deepcopy
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.back_track(nums, i + 1, track)
            track.pop()


if __name__ == "__main__":
    s = Solution()
    s.subsets([1,2,3])
