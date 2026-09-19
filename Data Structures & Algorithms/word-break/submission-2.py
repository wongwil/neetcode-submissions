class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {len(s) : True}
        n = len(s)
        def dfs(i):
            if i in mem:
                return mem[i]

            for w in wordDict:
                wLen = len(w)
                if (i+wLen) <= n and s[i:i+wLen] == w:
                    if dfs(i+wLen):
                        mem[i] = True
                        return True

            mem[i] = False
            return False

        return dfs(0)