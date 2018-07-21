'''
第一个错误的版本
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/53/
'''


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=1:
            return n
        begin,end =1,n
        while(begin<end):
            mid = int((begin+end)/2)
            if isBadVersion(mid):
                end = mid
            else:
                begin = mid + 1
                mid += 1
        return mid