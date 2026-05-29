class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0

        res = []
        while i < len(s):
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            strs = s[j+1:j+length+1]
            res.append(strs)

            i = j + length + 1
            j = i

        return res
