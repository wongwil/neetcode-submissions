class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dp = {}

        def dfs(r, c, prev):
            if (r < 0 or r == ROWS or c < 0 or c == COLS
            or matrix[r][c] <= prev):
                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            best = 0

            for d in DIRS:
                best = max(best, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))

            dp[(r,c)] = best
            
            return best

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))

        return res


            
