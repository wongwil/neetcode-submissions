class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        x = [0] * 26
        y = [0] * 26

        for c in s1:
            x[ord(c) - ord('a')] += 1
        
        for i in range(len(s1)):
            y[ord(s2[i]) - ord('a')] += 1

        if x == y:
            return True

        l = 0
        r = len(s1)-1

        while r < len(s2) - 1:
            y[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            y[ord(s2[r]) - ord('a')] += 1
            if x == y:
                return True


        return False
