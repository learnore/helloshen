# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : duilie
  Description : 队列总结
  Author      : chenyushencc@gmail.com
  date        : 2023/2/5 17:26
-------------------------------------------------
"""
from collections import deque
from queue import Queue


"""
239. 滑动窗口最大值（困难）
https://leetcode.cn/problems/sliding-window-maximum/description/
"""
class Solution:
    def __init__(self):
        self.windows = deque()

    def depush(self, n):
        while len(self.windows) and n > self.windows[-1]:       # while
            self.windows.pop()

        self.windows.append(n)

    def depop(self, n):
        if n == self.windows[0]:
            self.windows.popleft()

    def demax(self):
        return self.windows[0]

    def maxSlidingWindow(self, nums, k):
        res = []
        for ind, item in enumerate(nums):
            if ind < k - 1:
                self.depush(item)
            else:
                self.depush(item)
                res.append(self.demax())
                self.depop(nums[ind - k + 1])       # ind-k+1

        return res


if __name__ == "__main__":
    """
    双向队列
    """
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    dq.pop()
    dq.popleft()
    print(dq)       # deque([2])

    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    print(q.empty())       # 判空     False
    print(q.full())        # 判满     True
    if q.get():            # if 判断也会用掉一次，出一次队列
        pass
    print(q.full())        # False 因为 get 消耗了队列里的一个元素了
