'''
字符串中的第一个唯一字符
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/34/
'''


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        超出时间限制
        if len(s)==1:
            return 0
        if s !='':
            for i in range(len(s)):
                for j in range(len(s)):
                    if s[i] == s[j] and i!=j:
                        break
                    if j==len(s)-1:
                        return i
        return -1
        '''
        if s == '':
            return -1
        chars = 'abcdefghijklmnopqrstuvwxyz'
        char_list = [0]*26
        for i,char in enumerate(s):
            char_list[chars.index(char)] += 1
        ss = []
        for i,index in enumerate(char_list):
            if index==1:
                ss.append(s.index(chars[i]))
        if ss:
            return min(ss)
        return -1



if __name__=='__main__':
    strs= "dddccdbba"
    i = Solution().firstUniqChar(strs)
    print(i)       # False