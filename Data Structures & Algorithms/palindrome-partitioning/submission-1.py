class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subres = []

        def dfs(i):
            if i == len(s): # only add when we reached the end -> it means we were able to split
            # the whole s into palindrome substrings
                res.append(subres.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    subres.append(s[i:j+1]) # add current substring [i, j] to subresult
                    dfs(j+1) # start next backtrack for j+1
                    subres.pop()

        dfs(0)

        return res
            
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True