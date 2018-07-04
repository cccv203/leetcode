'''
删除链表的倒数第N个节点
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/42/
'''


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
        save_head = head
        origin_head = ListNode(0)
        origin_head.next = save_head
        for i in range(n):
            if head.next ==None:
                return origin_head.next.next
            head = head.next
        while(head.next !=None):
            head = head.next
            save_head = save_head.next
        save_head.next = save_head.next.next
        return origin_head.next













