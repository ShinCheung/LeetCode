# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# 给定的 n 保证是有效的
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        题意：删除链表中倒数第n个结点，尽量只扫描一遍。
        使用两个指针扫描，当第一个指针扫描到第N个结点后，
        第二个指针从表头与第一个指针同时向后移动，
        当第一个指针指向空节点时，另一个指针就指向倒数第n个结点的前一个点了
        '''
        res = ListNode(0)
        res.next = head
        tmp = res
        for _ in range(n):
            head = head.next
        while head != None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next