class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            max_profit = max(max_profit, prices[j] - prices[i]);
            if prices[j] < prices[i]:
                i = j
            
            j += 1
        
        return max_profit