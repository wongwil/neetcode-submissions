class Solution:
   

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def addCellToQueue(r, c, q):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == -1:
                return 
            
            q.append((r,c))
            visited.add((r,c))

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))


        dist = 0

        while q:
            levelLength = len(q)

            for i in range(levelLength):
                (r,c) = q.popleft()                
                grid[r][c] = dist

                addCellToQueue(r-1,c, q)
                addCellToQueue(r+1,c, q)
                addCellToQueue(r,c+1, q)
                addCellToQueue(r,c-1, q)

            dist += 1

        



