class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        profit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            else:
                profit = max(prices[i] - minPrice, profit)
        return profit