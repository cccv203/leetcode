'''
加一
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/27/
'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0,0)
        for i in range(len(digits)):
            digits[-i-1] += 1
            if digits[-i-1] == 10:
                digits[-i-1] = 0
                continue
            else:
                if digits[0] == 0:
                    digits.pop(0)
                return digits

if __name__=='__main__':
    nums=[9]
    i = Solution().plusOne(nums)
    print(nums)    # [1,0]
    print(i)       # [1,0]
