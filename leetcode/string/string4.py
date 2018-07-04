'''
有效的字母异位词
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/35/
'''


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        chars = 'abcdefghijklmnopqrstuvwxyz'
        s_list, t_list = [0] * 26, [0] * 26
        for i, char in enumerate(s):
            s_list[chars.index(char)] += 1
        for i, char in enumerate(t):
            t_list[chars.index(char)] += 1

        if s_list == t_list:
            return True
        return False


if __name__=='__main__':
    s = "anagram"
    t = "nagaram"
    i = Solution().isAnagram(s,t)
    print(i)       # False


