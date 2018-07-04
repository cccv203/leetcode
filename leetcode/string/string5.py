'''
验证回文字符串
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/36/
'''


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = '1234567890abcdefghijklmnopqrstuvwxyz'
        s = s.lower()
        ss = [s[i] for i in range(len(s)) if s[i] in chars]
        ss = "".join(ss)
        return ss == ss[::-1]


if __name__=='__main__':
    s = "A man, a plan, a canal: Panama"
    i = Solution().isPalindrome(s)
    print(i)       # False




