class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = defaultdict(int)
        n = len(s)

        for i in range(n):
            letters[s[i]] = i


        res = []               
        r,l  = 0, 0
        lastindex = letters[s[r]]
        while r < n:
            if r == lastindex:
                res.append(r - l + 1)
                r += 1
                l = r
                if r < n:
                    lastindex = letters[s[r]]
            else:
                lastindex = max(lastindex, letters[s[r]])
                r += 1
    

        return res
