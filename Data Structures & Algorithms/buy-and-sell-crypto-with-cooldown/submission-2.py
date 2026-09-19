class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, holding):
            if i >= n:
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            skip = dfs(i+1, holding)

            if holding:
                sold = prices[i] + dfs(i+2, False)
                dp[(i, holding)] = max(skip, sold)
            else:
                bought = - prices[i] + dfs(i+1, True)
                dp[(i, holding)] = max(skip, bought)

            return dp[(i, holding)]

        return dfs(0, False)
