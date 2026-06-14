class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window size - mostseen <= k
        l = 0
        res = 0
        mostseen = 0

        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            mostseen = max(mostseen, freq[s[r]])

            while r - l + 1 - mostseen > k:
                freq[s[l]] -= 1
                l += 1
                

            res = max(res, r - l + 1)
        return res