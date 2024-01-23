# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 6
  Description :

---------------- 用例 -----------------
输入
7 -2 6 6 9
6 7 -2 9 6
输出
-2 0 20 0 6

---------------- 用例 -----------------
输入
-3 12 6 8 9 -10 -7
8 12 -3 6 -10 9 -7
输出
0 3 0 7 0 2 0

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/12 16:47
-------------------------------------------------
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(pre_order, pre_start, pre_end, in_order, in_start, in_end):
    """ 根据 前序遍历和中序遍历，还原二叉树 """
    if pre_start > pre_end or in_start > in_end:
        return None

    root_val = pre_order[pre_start]
    # 如果前序遍历的前后索引都相等
    if pre_start == pre_end:
        return TreeNode(root_val)

    # 在中序遍历中找到 root_val 的索引，注意[]内是:冒号，不是逗号
    root_index = in_order[in_start: in_end+1].index(root_val) + in_start
    # 以该 root_index 作为划分点
    left_len = root_index - in_start

    root = TreeNode(val=root_val)
    root.left = build(pre_order, pre_start+1, pre_start+1+left_len-1,           # 索引的结点是细节
                      in_order, in_start, root_index-1)
    root.right = build(pre_order, pre_start+1+left_len-1 +1, pre_end,           # 索引的结点是细节
                       in_order, root_index+1, in_end)

    return root


def tree_sum(root):
    """ 计算不包含根数值的和 """
    if not root:
        return 0

    if root.left:
        root_left_val = root.left.val
    else:
        root_left_val = 0

    if root.right:
        root_right_val = root.right.val
    else:
        root_right_val = 0

    return tree_sum(root.left) + root_left_val + tree_sum(root.right) + root_right_val


def pre_search(root):
    """ 前序遍历一遍，修改每个根节点的值 """
    if not root:
        return None

    root.val = tree_sum(root)
    pre_search(root.left)
    pre_search(root.right)
    return root


results = []
def in_search(root):
    """ 中序遍历，输出 """
    if not root:
        return None

    in_search(root.left)
    results.append(root.val)
    in_search(root.right)

    return root


if __name__ == "__main__":
    in_order = list(map(int, input().split(" ")))
    pre_order = list(map(int, input().split(" ")))
    root = build(pre_order, 0, len(pre_order)-1, in_order, 0, len(in_order)-1)
    root = pre_search(root)

    in_search(root)
    print(" ".join([f"{i}" for i in results]))
