# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 7
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2024/1/7 12:15
-------------------------------------------------
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def total_time_to_receive_whisper(root):
    if not root:
        return 0

    left = total_time_to_receive_whisper(root.left)
    right = total_time_to_receive_whisper(root.right)

    return max(left, right) + root.val


if __name__ == "__main__":
    # 构建示例的二叉树结构
    root = TreeNode(0)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(3)
    root.right.left.right = TreeNode(2)

    # 计算悄悄话传递时间并输出结果
    result = total_time_to_receive_whisper(root)
    print(result)
