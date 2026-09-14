class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        

        bestlen = 0
        res = 0
        # odd length
        for c in range(n):
            l = c
            r = c

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > bestlen:
                    bestlen = r - l + 1
                    res = s[l:r+1]

                l -= 1
                r += 1

        # even
        for c in range(n):
            l = c
            r = c + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > bestlen:
                    bestlen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res