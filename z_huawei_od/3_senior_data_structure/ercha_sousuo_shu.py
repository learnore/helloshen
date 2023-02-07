# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : ercha_sousuo_shu
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/2/7 8:30
-------------------------------------------------
"""


"""
230. 二叉搜索树中第K小的元素
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
"""
class Solution:

    def __init__(self):
        self.zhongxu_bianli = []

    def kthSmallest(self, root, k):
        # 解题思路：利用二叉搜索树符合左子树小于根节点，右子树大于根节点的逻辑
        self.zhongxu_paixu(root)
        return self.zhongxu_bianli[k - 1]

    def zhongxu_paixu(self, root):
        if not root:
            return

        self.zhongxu_paixu(root.left)
        self.zhongxu_bianli.append(root.val)
        self.zhongxu_paixu(root.right)


"""
538. 把二叉搜索树转换为累加树
https://leetcode.cn/problems/convert-bst-to-greater-tree/description/
"""
class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        # 本题要求：①反转二叉搜索树②并进行和的累计
        return self.build(root)

    def build(self, root):
        if not root:
            return

        # 右子树
        self.build(root.right)
        # 中序累加
        self.sum += root.val
        root.val = self.sum
        # 左子树
        self.build(root.left)

        return root


# TODO 东哥带你刷⼆叉搜索树（第⼆期） 待练习

if __name__ == "__main__":
    pass
