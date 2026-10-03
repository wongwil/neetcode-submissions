class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        zerorows = set()
        zerocols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zerorows.add(i)
                    zerocols.add(j)
                    
        for i in range(n):
            for j in range(m):
                if i in zerorows or j in zerocols:
                    matrix[i][j] = 0

        