'''
二维数组中的查找
https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
'''


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i,j = len(array)-1,0
        while(i>=0 and j>= 0 and i<len(array) and j<len(array[0])):
            if array[i][j] == target:
                return True
            if array[i][j]<target:
                j +=1
            else:
                i -=1
        return False