class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            res = 0
            while n:
                digit = n % 10

                res += digit ** 2

                n = n // 10
            return res

        seen = set()
        while True:
            seen.add(n)
            n = getSum(n)

            if n == 1:
                return True
                
            if n in seen:
                return False