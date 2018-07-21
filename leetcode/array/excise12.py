'''
杨辉三角
https://leetcode-cn.com/problems/pascals-triangle/description/
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        nums_total = [[1]]
        for i in range(numRows-1):
            nums = nums_total[-1]
            temp = [1]
            for j in range(len(nums)-1):
                temp.append(nums[j]+nums[j+1])
            temp.append(1)
            nums_total.append(temp)
        return nums_total