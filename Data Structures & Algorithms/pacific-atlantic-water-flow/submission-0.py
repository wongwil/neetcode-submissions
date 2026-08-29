class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacifset = set()
        atlset = set()

        def dfs(r, c, myset, prevHeight):
            if (r < 0 or c < 0 or c >= COLS or r >= ROWS or (r,c) in myset
                or heights[r][c] < prevHeight):
                return

            myset.add((r,c))

            height = heights[r][c]
            dfs(r-1, c, myset, height)
            dfs(r+1, c, myset, height)
            dfs(r, c-1, myset, height)
            dfs(r, c+1, myset, height)


        # top
        for c in range(COLS):
            dfs(0, c, pacifset, 0)

        # left
        for r in range(ROWS):
            dfs(r, 0, pacifset, 0)

        # bottom
        for c in range(COLS):
            dfs(ROWS-1, c, atlset, 0)

        # right
        for r in range(ROWS):
            dfs(r, COLS-1, atlset, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacifset and (r,c) in atlset:
                    res.append((r,c))

        return res
            