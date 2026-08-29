class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        q = deque()

        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    time = -1

        def addNeigh(r,c, q):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or (r,c) in visited or grid[r][c] != 1):
                return

            visited.add((r,c))
            q.append((r,c))

        
        while q:
            for i in range(len(q)):
                (r,c) = q.popleft()

                grid[r][c] = 2
                addNeigh(r-1,c, q)
                addNeigh(r+1,c, q)
                addNeigh(r,c+1, q)
                addNeigh(r,c-1, q)

            time += 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time