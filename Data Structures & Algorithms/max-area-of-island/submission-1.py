class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS 
            or (r,c) in visited or grid[r][c] == 0):
                return 0

            # else it means path continues
            area = 1
            
            visited.add((r,c))

            area += dfs(r-1, c)
            area += dfs(r+1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))


        return res


