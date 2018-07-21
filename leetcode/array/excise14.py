'''
两数之和 II - 输入有序数组
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)==0:
            return None
        left,right = 0,len(numbers)-1

        while left<right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            if numbers[left] + numbers[right] < target:
                left +=1
            else:
                right -=1
        return None