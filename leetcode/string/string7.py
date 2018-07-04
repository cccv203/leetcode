'''
实现strStr()
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/38/
'''


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__=='__main__':
    haystack = "hello"
    needle = "ll"
    i = Solution().strStr(haystack,needle)
    print(i)       # False











