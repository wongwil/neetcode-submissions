class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = []

        for _ in range(n):
            row = ['.'] * n
            board.append(row)

        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if self.isFree(i, c, board):
                    board[i][c] = 'Q'
                    dfs(i+1,)
                    board[i][c] = '.'

        dfs(0)

        return res

    def isFree(self, r, c, board):
        # check vertical (above)
        i = r - 1
        j = c
        while i >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1


        # check \ diagonal
        i = r - 1
        j = c - 1

        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # check / diagonal

        i = r - 1
        j = c + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        return True
    