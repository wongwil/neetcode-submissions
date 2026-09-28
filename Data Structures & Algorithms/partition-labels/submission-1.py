class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = defaultdict(int)
        n = len(s)

        for i in range(n):
            letters[s[i]] = i


        res = []               
        r,l  = 0, 0
        lastindex = 0
        while r < n:
            lastindex = max(lastindex, letters[s[r]])

            if r == lastindex:
                res.append(r - l + 1)
                l = r + 1

            r += 1
    

        return res
