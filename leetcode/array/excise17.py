'''
存在重复元素 II
https://leetcode-cn.com/problems/missing-number/description/
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        key_val = {}
        for i in range(len(nums)):
            if nums[i] in key_val.keys():
                if i - key_val[nums[i]]>k:
                    return False
                else:
                    key_val[nums[i]] = min([i,key_val[nums[i]]])
            else:
                key_val[nums[i]] = i
        return True


if __name__ == '__main__':
    nums = [1,2,3,1]
    i = Solution().containsNearbyDuplicate(nums,3)
    print(nums)  # [1,0]
    print(i)  # [1,0]