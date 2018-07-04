'''
环形链表
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/46/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def stringToListNode(input):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        head_slow,head_fast = head,head
        while(head_fast.next!=None):
            head_fast = head_fast.next
            if head_fast.next is None:
                break
            head_slow,head_fast = head_slow.next,head_fast.next
            if head_slow == head_fast:
                return True
        return False
