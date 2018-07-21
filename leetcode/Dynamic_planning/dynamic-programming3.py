'''
最大子序和
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/56/
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[i-1]>=0:
                dp.append(dp[i-1]+nums[i])
            else:
                dp.append(nums[i])
        return max(dp)
