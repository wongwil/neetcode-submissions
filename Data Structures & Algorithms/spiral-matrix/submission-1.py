class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
        n, m = len(matrix), len(matrix[0])

        steps = [m, n-1] # (hor, vert)
        i, j = 0, -1
        currdir = 0

        res = []

        while len(res) < n*m:
            if dirs[currdir] == (0,1) or dirs[currdir] == (0, -1):
                 # horizontal 
                for step in range(steps[0]):
                    j += dirs[currdir][1]
                    res.append(matrix[i][j])
                steps[0] -= 1
            else:
                # vertical
                for step in range(steps[1]):
                    i += dirs[currdir][0]
                    res.append(matrix[i][j])
                steps[1] -= 1
            
            currdir += 1
            currdir %= 4

        return res

