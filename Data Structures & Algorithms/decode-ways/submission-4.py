class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        mem = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0

            c = s[i]

            if c == "0":
                return 0

            if mem[i] != -1:
                return mem[i]

            res = dfs(i+1)

            if i < n - 1 and ((s[i] == "1" and s[i+1] in "0123456789") or (s[i] == "2" and s[i+1] in "0123456")):
                    res += dfs(i+2)
               
            mem[i] = res
            return res
        
        return dfs(0)