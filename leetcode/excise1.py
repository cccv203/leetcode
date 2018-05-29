'''
从排序数组中删除重复项
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/21/
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:  ##防止空列表报错
            i = 0
            for _ in range(1,len(nums)):
                k=0
                for j in range(i+1, len(nums)):
                    if nums[j + k] == nums[i]:
                        del nums[j + k]
                        k-=1
                    else:
                        i += 1
                        break
            return i+1
        else:
            return 0
if __name__=='__main__':
    nums=[0,0,0,1,2,3,3,3,3]
    i = Solution().removeDuplicates(nums)
    print(nums)
    print(i)