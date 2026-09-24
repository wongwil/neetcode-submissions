class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            # i points at s
            # j points at t
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i,j) in dp:
                return dp[(i, j)]
            
            # we can skip it
            res = dfs(i+1, j)

            if s[i] == t[j]:
                # we can take it 
                res += dfs(i+1, j+1)

            dp[(i, j)] = res
            return res

        return dfs(0, 0)
                

            