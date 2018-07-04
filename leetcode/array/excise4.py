'''
存在重复
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/24/
'''


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums:
            nums_tuple = dict(zip(nums,[0]*len(nums)))
            return len(nums_tuple.keys()) != len(nums)
        else:
            return False
