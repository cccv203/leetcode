'''
反转链表
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/43/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next == None:
                return head
            save_list = ListNode(head.val)
            while(head.next!=None):
                temp = ListNode(head.next.val)
                temp.next,save_list = save_list,temp
                head = head.next
            return temp
        return None








