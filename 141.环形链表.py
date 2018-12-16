# 给定一个链表，判断链表中是否有环。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 快慢指针找环，快指针一次走两步，慢指针一次走一步，两个指针碰撞时（meet），说明找到环
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 快慢指针判断是否有环
        if not head:
            return False
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
