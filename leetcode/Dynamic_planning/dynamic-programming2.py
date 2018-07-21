'''
买卖股票的最佳时机
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/55/
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        price_diff = []
        for i in range(len(prices)-1):
            price_diff.append(prices[i+1] - prices[i])
        max_price,price = 0,0
        for diff in price_diff:
            price += diff
            if price < 0:
                price = 0
            max_price = max([price,max_price])
        return max_price
