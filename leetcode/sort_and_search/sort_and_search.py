'''
合并两个有序数组
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/52/
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if nums1 is None or nums2 is None:
            return
        for i in range(m+n-1,-1,-1):
            if n==0:
                return
            if m==0:
                nums1[i] = nums2[n-1]
                n -= 1
            elif nums1[m-1] <= nums2[n-1]:
                nums1[i] = nums2[n-1]
                n -= 1
            elif nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1


if __name__=='__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    i = Solution().merge(nums1,m,nums2,n)
    print(nums1)       # 4