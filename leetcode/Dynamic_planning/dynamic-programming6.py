'''
拼接最大数
https://leetcode-cn.com/problems/create-maximum-number/description/
'''


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_num = 0
        result = []
        for i in range(k):
            num1_index, num2_index = 0,0
            for j in nums1[num1_index:len(nums1)+len(nums2)-i]:

            max(nums1[num1_index:],nums2[num2_index:])


















