'''
移动零
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/28/
'''



class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                continue
            else:
                i += 1
        # nums.extend([0] * (i-1))


if __name__=='__main__':
    nums=[0,1,0,3,12]
    i = Solution().moveZeroes(nums)
    print(nums)    # [1,0]
    print(i)       # [1,0]


