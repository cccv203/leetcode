'''
杨辉三角 II
https://leetcode-cn.com/problems/pascals-triangle-ii/description/
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        temp = [1]
        for i in range(rowIndex+1):
            nums = temp
            temp = [1]
            for j in range(len(nums)-1):
                temp.append(nums[j]+nums[j+1])
            temp.append(1)
        return nums

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    i = Solution().getRow(3)
    print(nums)  # [1,0]
    print(i)  # [1,0]
