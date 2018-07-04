class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        超出时间限制
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]
        '''
        a = nums[0]
        for i in range(len(nums)-1):
            a ^= nums[i+1]
        return a

if __name__=='__main__':
    nums=[7,1,5,3,6,4,7,1,5,3,6,4,0]
    i = Solution().singleNumber(nums)
    print(nums)    # [7, 1, 5, 3, 6, 4]
    print(i)       # 7
