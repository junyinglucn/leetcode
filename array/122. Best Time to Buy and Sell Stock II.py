class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                res += tmp
        return res
