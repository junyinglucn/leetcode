# Solution A
class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                continue
            for j in prices[i + 1:]:
                tmp = j - prices[i]
                if tmp > res:
                    res = tmp
        return res


# Solution B
class Solution:
    def maxProfit(self, prices):
        l = len(prices)
        res = 0
        dp = [0] * l
        prices = prices + [0]
        for i in range(l - 2, -1, -1):
            if prices[i + 1] > dp[i + 1]:
                dp[i] = prices[i + 1]
            else:
                dp[i] = dp[i + 1]
            res = max(res, (dp[i] - prices[i]))
        return res


# Solution C
class Solution:
    def maxProfit(self, prices):
        minprice = float('inf')
        res = 0
        for price in prices:
            res = max(res, price - minprice)
            minprice = min(minprice, price)
        return res
