# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 560_subarray-sum-equals-k
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/2/3 9:31
-------------------------------------------------
"""


class Solution:
    def subarraySum(self, nums, k):
        res = 0
        """
        # 构造前缀和
        pre_sum = [0]       # 这里不加 0 的话，后面就得用一部分代码判断，甚至无法判断到只有一个元素的情况
        sum_res = 0
        for i in nums:
            sum_res += i
            pre_sum.append(sum_res)

        # 暴力循环，会超时，导致无法AC
        xxxxxxxxxxxxxxxxxxx
        for i in range(1, len(nums)+1):
            for j in range(i):
                if pre_sum[i] - pre_sum[j] == k:
                    res += 1
        xxxxxxxxxxxxxxxxxxx
        """
        pre_sum = {}
        sum_res = 0
        pre_sum[0] = 1
        for i in nums:
            sum_res += i
            check_value = sum_res - k  # 思路：k = sum_res - check_value

            if check_value in pre_sum:
                res += pre_sum[check_value]

            pre_sum[sum_res] = pre_sum.get(sum_res, 0) + 1

        return res


if __name__ == "__main__":
    pass
