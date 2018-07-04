'''
反转字符串
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/32/
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[-1::-1]


if __name__=='__main__':
    strs= "hello"
    i = Solution().reverseString(strs)
    print(i)       # False