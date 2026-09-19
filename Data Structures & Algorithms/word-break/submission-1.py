class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        minLen = min(len(w) for w in wordDict)

        mem = {}
        def dfs(strRemaining):
            if strRemaining in mem:
                return mem[strRemaining]

            if strRemaining == "":
                return True

            if len(strRemaining) < minLen:
                return False

            for w in wordDict:
                wLen = len(w)
                if strRemaining[:wLen] == w:
                    res = dfs(strRemaining[wLen:])
                    mem[strRemaining] = True
                    if res:
                        return True
            mem[strRemaining] = False
            return False

        return dfs(s)