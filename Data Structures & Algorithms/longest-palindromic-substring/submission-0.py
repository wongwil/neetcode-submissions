class Solution:
    def longestPalindrome(self, s: str) -> str:
        # define dp[i][j] := s[i:j+1] is a palindrome
        # dp[i][j] = 1 iff dp[i+1][j-1] == 1 AND 
        # s[i] == s[j]
        # OR
        # s[i] == s[j] and substring len(s[i:j+1)] is 1, 2 or 3
        # because just one letter (always pali), 2 has no center, 3 can any letter be a center
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # dp[i][j] relies on i+1 => need to iterate i from n to 0
        # relies on j-1 => need to iterate j from 0 to n
        res = ""
        bestlen = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > bestlen:
                        bestlen = j - i + 1
                        res = s[i:j+1]

        return res

        