class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = {}

        for i, c in enumerate(s):
            letters[c] = i

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
