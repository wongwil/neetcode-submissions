class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            res = 0
            for c in str(n):
                res += int(c) ** 2

            return res
        curr = n
        seen = set()
        while True:
            seen.add(curr)
            curr = getSum(curr)
            if curr == 1:
                return True
            
            if curr in seen:
                return False