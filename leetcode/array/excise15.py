'''
求众数
https://leetcode-cn.com/problems/majority-element/description/
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return []
        num_major = []
        for i in nums:
            if len(num_major) == 0:
                num_major.append(i)
                continue
            if i != num_major[-1]:
                num_major.pop()
                continue
            num_major.append(i)

        return num_major[0]

