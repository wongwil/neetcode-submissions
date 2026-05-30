class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        i = j = 0
        
        res = []
        while i < len(s):
            while s[j] != "#":
                j += 1

            size = int(s[i:j])
            
            st = s[j+1:j+1+size]
            res.append(st)

            i = j+1+size
            j = i

        return res