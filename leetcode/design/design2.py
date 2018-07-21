'''
Shuffle an Array
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/24/design/58/
'''


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        import random
        import copy
        self.origin_nums,self.nums = nums,copy.deepcopy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        for i in range(len(self.nums)):
            t = i + random.randint(0,len(self.nums)-i-1)
            self.nums[t],self.nums[i] = self.nums[i],self.nums[t]
        return self.nums