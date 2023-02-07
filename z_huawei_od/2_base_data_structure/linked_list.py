# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : linked_list
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/2/6 9:36
-------------------------------------------------
"""
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/
"""
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1, None)
        p = dummy

        while list1 and list2:
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next

            p = p.next

        if list1:
            p.next = list1

        if list2:
            p.next = list2

        return dummy.next


"""
23. 合并K个升序链表 - 解题思路：使用小顶堆（先全部加入，再逐一 pop）
https://leetcode.cn/problems/merge-k-sorted-lists/
"""
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        min_heapq = []
        heapq.heapify(min_heapq)
        for item in lists:
            while item:
                heapq.heappush(min_heapq, item.val)
                item = item.next

        dummy = ListNode(-1, None)
        p = dummy
        while min_heapq:
            p.next = ListNode(val=heapq.heappop(min_heapq))
            p = p.next

        return dummy.next


"""
141. 环形链表 - 解题思路：快慢指针
https://leetcode.cn/problems/linked-list-cycle/description/
"""
class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False

        # 快慢指针
        fast, slow = head, head
        while fast:  # 这里还只能用 快指针 做判断依据，用 慢指针 会出现报错的情况
            fast = fast.next
            if not fast:
                return False

            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True

        return False


"""
142. 环形链表 II（中等） - 解题思路：快慢指针
https://leetcode.cn/problems/linked-list-cycle-ii/description/
"""
class Solution:
    def detectCycle(self, head):
        # 使用快慢指针 ①相遇后，慢指针走了 n 步，快指针走了 2n 步；②重新让快指针从开始出发，慢指针继续出发，再次相遇的时候就是循环的节点
        fast, slow = head, head
        # ①
        while fast:
            fast = fast.next
            if not fast:
                return None  # -1

            fast = fast.next
            slow = slow.next

            if not fast:  # 防止 fast = slow = None
                return None  # -1

            if fast == slow:
                break

        # ②
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast


"""
876. 链表的中间结点 - 解题思路：快慢指针
https://leetcode.cn/problems/middle-of-the-linked-list/description/
"""
class Solution:
    def middleNode(self, head):
        # 快慢指针
        fast, slow = head, head
        while fast and fast.next:  # 不是 fast.next and fast.next.next
            fast = fast.next.next
            slow = slow.next

        return slow


"""
19. 删除链表的倒数第 N 个结点（中等） - 解题思路：相同间隔法，类似使用双指针
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
"""
class Solution:
    def removeNthFromEnd(self, head, n: int):
        # 相同间隔法，类似使用双指针
        # ①两个指针的间隔是 n，那么当后一个指针指到末尾的时候，第一个指针就是要删除的节点
        # ②node.next = node.next.next 即可删除节点 node
        dummy = ListNode()  # 必须要先创建
        dummy.next = head

        first, second = dummy, dummy
        # first 先走 n 步
        for i in range(n + 1):  # +1 是因为 dummy 自己初始化的时候占了一个位置
            first = first.next

        while first:  # 不是 first.next
            first = first.next
            second = second.next

        second.next = second.next.next

        # dummy = ListNode()      # 如果在这里创建会出现错误哦，会导致 second.next = second.next.next 时可能出现 second 为 None 的情况
        # dummy.next = head

        # 返回结果
        return dummy.next


"""
160. 相交链表 - 解题思路：判断的是倒数/尾部相同的，那就把两个链表都走一遍/合并，就能保证有重复的时候肯定是相同的（headA headB 最后的指定都是 None，所以肯定有至少一个（None）相同的）
https://leetcode.cn/problems/intersection-of-two-linked-lists/description/
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1


if __name__ == "__main__":
    pass
