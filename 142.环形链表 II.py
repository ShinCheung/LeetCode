# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null
# 说明：不允许修改给定的链表。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 快慢指针找环，快指针一次走两步，慢指针一次走一步，两个指针碰撞时（meet），说明找到环
# 再用两个指针，一个从meet开始，一个从head开始，每次都只走一步，再次碰撞时，是环的起始节点
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 此方法太慢了
        nodeList = []
        while head:
            if head in nodeList:
                return head
            nodeList.append(head)
            head = head.next
        return None
    
    # 两步:首先通过快慢指针的方法判断链表是否有环；接下来如果有环，则寻找入环的第一个节点
    def detectCycle1(self, head):
        # 快慢指针判断是否有环
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # 如果有环，则寻找入环的第一个节点
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
    
    def detectCycle2(self, head):
        # 快慢指针判断是否有环
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果有环，则寻找入环的第一个节点
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
            
