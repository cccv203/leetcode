'''
回文链表
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/45/
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


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        head_copy = head
        if head.next == None:
            return True
        save_list = ListNode(head.val)
        while head.next != None:
            temp = ListNode(head.next.val)
            temp.next, save_list = save_list, temp
            head = head.next
        while head_copy.next !=None:
            if head_copy.val != temp.val:
                return False
            head_copy = head_copy.next
            temp = temp.next
        return True

if __name__=='__main__':
    l1 = [1,2,4,2,1]
    i = Solution().isPalindrome(stringToListNode(l1))
    print(i)       # False
