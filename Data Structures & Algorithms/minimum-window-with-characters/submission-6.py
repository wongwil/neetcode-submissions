class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetmap = defaultdict(int)

        for c in t:
            targetmap[c] += 1

        windowmap = defaultdict(int)

        matches = 0
        goalmatches = len(targetmap)

        minimum = float('inf')
        res = ""
        l = 0
        for r in range(len(s)):
            c = s[r]
            windowmap[c] += 1

            if windowmap[c] == targetmap[c]:
                matches += 1

            while matches == goalmatches:
                winsize = r - l + 1
                if winsize < minimum:
                    minimum = winsize
                    res = s[l:r+1]

                windowmap[s[l]] -= 1
                if s[l] in targetmap and windowmap[s[l]] < targetmap[s[l]]:
                    matches -= 1

                l += 1

        return res


            