'''
合并两个有序链表
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/44/
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is not None:
            return l2
        if l2 is None and l1 is not None:
            return l1
        if l1 is None and l2 is None:
            return None

        save_list,temp = ListNode(0),ListNode(0)
        save_list.next = temp
        while(l1!=None and l2!=None):
            if l1.val<=l2.val:
                temp.next = ListNode(l1.val)
                l1,temp = l1.next,temp.next
            else:
                temp.next = ListNode(l2.val)
                l2, temp = l2.next, temp.next
        l3 = l1 if l2==None else l2
        while(l3.next!=None):
            temp.next=ListNode(l3.val)
            l3, temp = l3.next, temp.next
        temp.next = ListNode(l3.val)
        return save_list.next.next

if __name__=='__main__':
    l1 = [1,2,4]
    l2 = [1,3,3]
    i = Solution().mergeTwoLists(stringToListNode(l1),stringToListNode(l2))
    print(listNodeToString(i))       # False


