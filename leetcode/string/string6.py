'''
字符串转整数（atoi）
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/37/
'''


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = '-+1234567890'
        str = str.strip()
        if str == '' or str[0] not in nums:
            return 0
        if len(str)>1 and str[1] in nums[:2]:
            return 0
        str_num = []
        for i in range(1,len(str)):
            if str[i] not in nums[2:]:
                break
            str_num.append(str[i])
        str_num.insert(0,str[0])
        if str_num == ['-'] or str_num == ['+']:
            return 0

        str_num = int("".join(str_num))
        if str_num < -2**31:
            return -2**31
        if str_num>2**31-1:
            return 2**31-1
        return str_num


if __name__=='__main__':
    s = "+-1"
    i = Solution().myAtoi(s)
    print(i)       # False







