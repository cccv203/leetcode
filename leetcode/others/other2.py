'''
汉明距离
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/65/
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x<0 or x>2**31 or y<0 or y>2**31:
            return
        n =x^y
        i=0
        while n!=0:
            n = n &(n-1)
            i += 1
        return i