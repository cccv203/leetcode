'''
最小栈
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/24/design/59/
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack= []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.stack)==1:
            self.minstack.append(x)
        elif x <self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        """
        :rtype: void
        """
        assert len(self.stack) >= 1
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        assert len(self.stack)>=1
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        assert len(self.minstack) >= 1
        return self.minstack[-1]