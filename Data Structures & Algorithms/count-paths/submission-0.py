class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mem = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if i >= n or j >= m:
                return 0

            if mem[i][j] != -1:
                return mem[i][j]

            if i == n-1 and j == m - 1:
                return 1

            mem[i][j] = dfs(i+1, j) + dfs(i, j+1)

            return mem[i][j]

        return dfs(0,0)