# 反转一个单链表。
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head是要插入到新链表的节点
        # tmp是临时保存的head的next
        # last是指pre_node
        last = None
        while head:
            tmp = head.next     # tmp保存下一次要插入的节点
            head.next = last    # 把pHead插入到last中
            last = head         # 纠正头结点last的指向
            head = tmp          # head指向下一次要插入的节点
        return last