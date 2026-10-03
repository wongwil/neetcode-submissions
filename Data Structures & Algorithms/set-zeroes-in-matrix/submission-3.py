class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        firstRowIsZero = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # set top border to 0

                    if i == 0: # if we encounter a 0 in first 0, we ignore it and rewrite it at the end
                        firstRowIsZero = True
                    else:
                        matrix[i][0] = 0

        # left border
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0

        # top border
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        # corner is 0 could be from row or column or original
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0

        if firstRowIsZero:
            for j in range(m):
                matrix[0][j] = 0

        