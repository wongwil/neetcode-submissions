class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = []
        dp = {}
        def dfs(i, holding): # return maximum profit achievable at i
            if i >= len(prices):
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            # skip current
            res = dfs(i+1, holding)

            # buy
            if not holding:
                bought = dfs(i+1, True) - prices[i]
                res = max(bought, res)
            else:
                # sell
                sold = dfs(i+2, False) + prices[i]
                res = max(sold, res)
            
            dp[(i, holding)] = res
            return res

        return dfs(0, False)