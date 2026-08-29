class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or (r,c) in visited or board[r][c] == "X"):
                return

            visited.add((r,c))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        # top
        for c in range(COLS):
            dfs(0, c)

        # left
        for r in range(ROWS):
            dfs(r, 0)

        # right
        for r in range(ROWS):
            dfs(r, COLS-1)

        # bottom
        for c in range(COLS):
            dfs(ROWS-1, c)


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    board[r][c] = "X"

