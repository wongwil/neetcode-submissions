class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {i : -1 for i in range(amount+1)}
        dp[0] = 0
        def dfs(a):
            if dp[a] != -1:
                return dp[a]

            res = float("Inf") # any large number
            for c in coins:
                if c <= a:
                    res = min(res, 1 + dfs(a - c))
            dp[a] = res
            return res

        res = dfs(amount)
        if res == float("Inf"):
            return -1
        
        return res