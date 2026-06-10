class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        res = 0

        for price in prices:
            currprofit = max(0, price - bestbuy)
            res = max(res, currprofit)

            if price < bestbuy:
                bestbuy = price

        return res
            
