class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(i, r, c):
            if r < 0 or c < 0 or c >= COLS or r >= ROWS:
                return False

            char = board[r][c]

            if char == "#" or char != word[i]:
                return False

            if i == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            if dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1):
                return True

            board[r][c] = temp

        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True


        return False