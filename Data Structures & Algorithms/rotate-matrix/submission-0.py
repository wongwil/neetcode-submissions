class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (0,0) => (0, 2)
        # (0,1) => (1, 2)
        # (0,2) => (2, 2)
        # (1,2) => (2, 1)
        # (2,0) => (0,0)
        # (1,0) => (0,1)

        # derive
        # (i, j) => (j, n-1-i)

        # note that (i,j) => (j,i) is the transposition
        # the (,n-1-i) is just reversing each row

        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()