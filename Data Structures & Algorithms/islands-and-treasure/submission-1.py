class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        def addNeighbour(r, c, q):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or grid[r][c] == -1 or (r,c) in visited):
                return

            q.append((r,c))
            visited.add((r,c)) # mark it as visited so it doesn't gets added from another call

        dist = 0
        while q:
            levelLength = len(q)

            for i in range(levelLength):
                (r,c) = q.popleft()
                grid[r][c] = dist

                addNeighbour(r+1,c, q)
                addNeighbour(r-1,c, q)
                addNeighbour(r,c-1, q)
                addNeighbour(r,c+1, q)

            dist += 1

