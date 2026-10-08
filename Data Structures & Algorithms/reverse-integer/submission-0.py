class Solution:
    def reverse(self, x: int) -> int:
        maxint = 2**31
        minint = (-2)**31
        
        negative = x < 0
        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            x = x // 10
            
            if res * 10 + digit > maxint:
                return 0
                
            res = res * 10 + digit

        if negative:
            res = -res

        return res