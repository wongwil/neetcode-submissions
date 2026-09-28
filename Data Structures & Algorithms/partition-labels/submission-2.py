class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = defaultdict(int)
        n = len(s)

        for i in range(n):
            letters[s[i]] = i

        end = 0
        ctr = 0

        res = []
        for i, c in enumerate(s):
            end = max(letters[c], end)
            ctr += 1

            if i == end:
                res.append(ctr)
                ctr = 0

        return res
