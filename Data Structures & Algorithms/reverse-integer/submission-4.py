class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        maxint = 2**31 if negative else 2**31 - 1
        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            x = x // 10
            
            if res > maxint // 10 or (res == maxint // 10 and digit > maxint % 10):
                return 0

            res = res * 10 + digit

        if negative:
            res = -res

        return res