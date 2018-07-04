'''
旋转数组
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/23/
'''


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        时间超出限制
        for _ in range(k%len(nums)):
            t = nums[-1]
            for i in range(len(nums),0,-1):
                nums[i-1] = nums[i-2]
            nums[0] = t
        '''
        k = k%len(nums)
        for i in range(int((len(nums) - k)/2)):
            nums[i], nums[-k-i-1] = nums[-k-i-1], nums[i]
        for i in range(int(k/2)):
            nums[-i-1], nums[-k+i] = nums[-k+i], nums[-i-1]
        nums.reverse()




if __name__=='__main__':
    nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]

    i = Solution().rotate(nums,4)
    print(nums)    # [7, 1, 5, 3, 6, 4]
    # print(i)       # 7