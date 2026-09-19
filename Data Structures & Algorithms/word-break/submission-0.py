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
                    mem[strRemaining[wLen:]] = res
                    if res:
                        return True

            return False

        return dfs(s)