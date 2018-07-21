'''
三数之和
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/75/
'''


class Solution(object):

    def twosum(self,nums,target):
        if not nums:
            return
        key_map = {}
        twosum = []
        for index, value in enumerate(nums):
            if (target - value) in key_map.keys():
                twosum.append([target - value, value])
            else:
                key_map[value] = index
        return twosum

    def is_same_sum(self,nums1,nums2):
        if len(nums1) != len(nums2):
            return False
        nums1.sort()
        nums2.sort()

        if nums1 == nums2:
            print(nums1, nums2)
            return True
        return False

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        threesum = []
        for index,value in enumerate(nums):
            twosum = self.twosum(nums[index+1:],-value)
            if twosum:
                for two in twosum:
                    two.append(value)
                    if threesum:
                        for three in threesum:
                            if not self.is_same_sum(two,three):
                                # print(threesum)
                                # print(two)
                                threesum.append(two)
                    else:
                        threesum.append(two)
        return threesum

if __name__=='__main__':
    nums=[-1,0,1,2,-1,-4]
    i = Solution().threeSum(nums)
    print(i)       # [1,0]