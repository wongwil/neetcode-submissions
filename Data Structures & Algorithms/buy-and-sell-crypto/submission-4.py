class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        i, j = 0, 1
        res = 0
        while j < len(prices):
            res = max(res, prices[j] - prices[i])

            if prices[i] > prices[j]:
                i = j
            
            j += 1
        
        return res