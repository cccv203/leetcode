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




