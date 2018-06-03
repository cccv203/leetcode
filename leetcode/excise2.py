class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profift = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                max_profift += prices[i+1] - prices[i]
        return max_profift


if __name__=='__main__':
    nums=[7,1,5,3,6,4]
    i = Solution().maxProfit(nums)
    print(nums)    # [7, 1, 5, 3, 6, 4]
    print(i)       # 7


