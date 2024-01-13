# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 5
  Description : 根据 后、中缀二叉树 恢复二叉树

-------- 用例 ----------
输入
CBEFDA CBAEDF
输出
ABDCEF

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/11 16:20
-------------------------------------------------
"""
from queue import Queue


results = []
my_queue = Queue()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(my_queue):
    """ 广度优先遍历树，队列 """
    # base case
    if my_queue.empty():
        return

    root = my_queue.get()
    results.append(root.val)
    if root.left:
        my_queue.put(root.left)
    if root.right:
        my_queue.put(root.right)

    bfs(my_queue)


def build(post_order, post_start, post_end, in_order, in_start, in_end):
    """ 根据 后序遍历和中序遍历，还原二叉树 """
    if post_start > post_end:
        return

    root_value = post_order[post_end]
    if post_start == post_end:
        return TreeNode(val=root_value)

    # root 值在中序排序中的 index（[:]顾前不顾后的原则别忘了in_end+1）
    root_index = in_order[in_start:in_end + 1].index(root_value) + in_start  # 注意偏移量
    left_len = root_index - in_start        # 表示有左子树的元素个数

    root = TreeNode(val=root_value)
    root.left = build(
        post_order, post_start, post_start+left_len-1,
        in_order, in_start, root_index - 1
    )
    root.right = build(
        post_order, post_start+left_len-1 +1, post_end - 1,
        in_order, root_index + 1, in_end
    )
    return root


if __name__ == "__main__":
    post_order, in_order = map(str, input().split(" "))
    post_order = [i for i in post_order]
    in_order = [i for i in in_order]
    root = build(post_order, 0, len(post_order)-1, in_order, 0, len(in_order)-1)

    my_queue.put(root)
    bfs(my_queue)
    print("".join(results))
