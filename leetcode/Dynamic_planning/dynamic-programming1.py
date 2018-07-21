'''
爬楼梯
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/54/
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        if n ==2:
            return 2
        f_n_1,f_n_2 = 2,1
        for i in range(3,n+1):
            steps = f_n_1+f_n_2
            f_n_2 = f_n_1
            f_n_1 = steps
        return steps