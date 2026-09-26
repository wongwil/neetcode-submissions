class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        # does p[j:] validate s[i:]?
        dp = {}
        def dfs(i, j):
            if j == n:
                return i == m

            if (i,j) in dp:
                return dp[(i,j)]

            valid = False
            if j < n - 1 and p[j+1] == "*":     
                # skip it (0 occurence)
                valid = valid or dfs(i, j+2)

                # if matches, then use it 
                if i < m and (s[i] == p[j] or p[j] == "."):
                    valid = valid or dfs(i+1, j)
            else:
                if i < m and(s[i] == p[j] or p[j] == "."):
                    valid = valid or dfs(i+1, j+1)

            dp[(i,j)] = valid

            return valid


        return dfs(0, 0)