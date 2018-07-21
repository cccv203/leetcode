


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        超出时间限制
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        '''

        '''
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums:
                x_index = nums.index(x)
                if x_index != i:
                    return [x_index,i]
        '''

        key_map = {}
        for index,value in enumerate(nums):
            if (target-value)in key_map.keys():
                return [key_map[target-value], index]
            else:
                key_map[value] = index


if __name__=='__main__':
    nums=[0,1,0,3,12]
    i = Solution().twoSum(nums,12)
    print(nums)    # [1,0]
    print(i)       # [1,0]