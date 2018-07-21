'''
位1的个数
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/64/
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while n!=0:
            n = n &(n-1)
            i += 1
        return i