'''
两个数组的交集 II
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/26/
'''


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = []
        for i in nums1:
            if i in nums2:
                nums3.append(i)
                nums2.remove(i)
        return nums3

if __name__=='__main__':
    nums=[7,1,5,3,6,4]
    i = Solution().intersect(nums,[2,4,5])
    print(nums)    # [7, 1, 5, 3, 6, 4]
    print(i)       # 7
