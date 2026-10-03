class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        n = len(matrix)
        m = len(matrix[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        currdir = 0
        curr = (0,0)

        visited.add(curr)
        res = [matrix[curr[0]][curr[1]]]
        while len(res) < n*m:
            nextentry = (curr[0] + dirs[currdir][0], curr[1] + dirs[currdir][1])

            if nextentry in visited or min(nextentry[0],nextentry[1]) == -1 or nextentry[0] == n or nextentry[1] == m:
                currdir += 1
                currdir %= 4
                nextentry = (curr[0] + dirs[currdir][0], curr[1] + dirs[currdir][1])

            curr = nextentry
            res.append(matrix[nextentry[0]][curr[1]])
            visited.add(curr)

        return res