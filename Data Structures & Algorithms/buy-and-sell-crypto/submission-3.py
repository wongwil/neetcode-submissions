class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        i, j = 0, 0
        res = 0
        while j < len(prices):
            while j < len(prices) and prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])
                j += 1
            
            i = j
            j = i+1
        
        return res