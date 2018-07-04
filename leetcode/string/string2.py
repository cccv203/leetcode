'''
颠倒整数
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/33/
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            x = int('-'+x[-1:0:-1])
        else:
            x = int(x[-1::-1])
        if (x > -2**31) & (x<2**31-1):
            return x
        else:
            return 0



if __name__=='__main__':
    strs= 1534236469
    i = Solution().reverse(strs)
    print(i)       # False