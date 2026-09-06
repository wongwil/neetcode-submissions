class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(-1, 0), (0, -1), (1,0), (0,1)]

        myheap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))

        while myheap:
            weight, row, col = heapq.heappop(myheap)

            if row == ROWS - 1 and col == COLS - 1:
                return weight

            for a, b in directions:
                y = row + a
                x = col + b

                if x < 0 or y < 0 or x >= COLS or y >= ROWS:
                    continue

                if (y, x) in visited:
                    continue

                weightNew = grid[y][x]
                heapq.heappush(myheap, (max(weightNew, weight), y, x))
                visited.add((y, x))

        return -1
            