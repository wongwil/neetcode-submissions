class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = {n : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                dp[i] = 0
                return dp[i]

            # for any other character we can continue
            dp[i] = dfs(i+1)

            # if s[i] is a 1 or 2, it could be 2 digits
            if i < n - 1:
                if s[i] == "1":
                    dp[i] += dfs(i+2)
                elif s[i] == "2" and s[i+1] in "0123456":
                    dp[i] += dfs(i+2)

            return dp[i]

        return dfs(0)

            