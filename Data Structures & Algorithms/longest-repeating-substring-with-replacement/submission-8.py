class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # res = 0
        # for l in range(len(s)):
        #     freq = defaultdict(int)
        #     maxseen = 0
        #     for r in range(l, len(s)):
        #         freq[s[r]] += 1
        #         maxseen = max(maxseen, freq[s[r]])

        #         if r - l + 1 - maxseen <= k:
        #             res = max(res, r - l + 1)
        
        # return res

        l = 0
        freq = defaultdict(int)
        mostseen = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            mostseen = max(mostseen, freq[s[r]])

            if r - l + 1 - mostseen > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

        