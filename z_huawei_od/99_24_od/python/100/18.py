# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 18
  Description : 递归 + 树 + 树的高度

🎃样例1
输入
5
5000 2000 5000 8000 1800
输出
3

🎃样例2
输入
3
5000 4000 3000
输出
3

🎃样例3
输入
9
5000 2000 5000 8000 1800 7500 4500 1400 8100
输出
4

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/9 12:15
-------------------------------------------------
"""


class TreeNode:
    """ 三叉树 """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None


def insert_node(root, num):
    """
    插入节点的递归函数
    本函数的意义：将 num 插入 root 这个树中
    """
    if not root:
        return TreeNode(num)

    if num < root.value-500:
        root.left = insert_node(root.left, num)     # 注意！！！insert_node() 函数的意义：将 num 插入 root.left 这个树中
        """ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # if root.left:
        #     insert_node(root.left)
        # else:
        #     root.left = TreeNode(num)
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX """
    elif num > root.value+500:
        root.right = insert_node(root.right, num)
    else:
        root.middle = insert_node(root.middle, num)

    return root


def root_high(root):
    """
    计算树的高度
    """
    if not root:
        return 0

    left_high = root_high(root.left)
    middle_high = root_high(root.middle)
    right_high = root_high(root.right)
    return max(left_high, middle_high, right_high) + 1


if __name__ == "__main__":
    # 输入描述
    N = int(input())  # 输入的数的个数
    nums = list(map(int, input().split()))  # 输入的数
    # 根据规则构造三叉搜索树
    root = None
    for num in nums:
        root = insert_node(root, num)
    # 输出树的高度
    print(root_high(root))
