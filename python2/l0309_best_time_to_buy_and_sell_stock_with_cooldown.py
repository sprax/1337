class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy, prev_buy, sell, prev_sell = -prices[0], 0, 0, 0
        for p in prices:
            prev_buy = buy
            buy = max(prev_sell-p, prev_buy)
            prev_sell = sell
            sell = max(prev_buy+p, prev_sell)
        return sell

