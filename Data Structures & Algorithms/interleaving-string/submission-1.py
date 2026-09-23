class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = {}

        def dfs(i, j, k):
            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            dp[(i, j, k)] = False
            # take from A
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1, j, k+1):
                dp[(i, j, k)] = True

            # take from B
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j+1, k+1):
                dp[(i, j, k)] = True 

            return dp[(i, j, k)] 

        return dfs(0, 0, 0)