'''
第三大的数
https://leetcode-cn.com/problems/third-maximum-number/description/
'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return
        first,second,third = -2**32,-2**32,-2**32
        for num in nums:
            if num>first:
                third = second
                second = first
                first=num
            if num>second and num<first:
                third=second
                second=num
            if num>third and num<second:
                third=num
        return third if (third!=-2**32 and third!=second) else first