'''
缺失数字
https://leetcode-cn.com/problems/missing-number/description/
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res



