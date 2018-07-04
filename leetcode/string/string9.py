'''
最长公共前缀
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/40/
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:
            return ''
        if len(strs)==1:
            return strs[0]
        min_len = min([len(chars) for chars in strs])
        for i in range(min_len):
            for chars in strs[1:]:
                if chars[i] != strs[0][i]:
                    if i==0:
                        return ''
                    return strs[0][:i]
        return strs[0][:min_len]

if __name__=='__main__':
    s = ["aa","a"]
    i = Solution().longestCommonPrefix(s)
    print(i)       # False






