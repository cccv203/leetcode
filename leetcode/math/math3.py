'''
3的幂
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/62/
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        if n==0 :
            return False
        while n!=1 :
            if n % 3 != 0:
                return False
            n = n/3
        return True
        '''
        
