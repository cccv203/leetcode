'''
打家劫舍
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/57/
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)

        dp = [nums[0], max([nums[0], nums[1]])]
        for i in range(2,len(nums)):
            dp.append(max([dp[i-2]+nums[i], dp[i-1]]))

        return dp[len(nums)-1]
