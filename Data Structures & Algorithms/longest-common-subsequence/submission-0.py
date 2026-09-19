class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if i == n or j == m:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            # matching characters
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
                return dp[i][j]

            # skip i or j
            dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[i][j]

        return dfs(0, 0)