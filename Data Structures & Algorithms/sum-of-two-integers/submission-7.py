class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            carry = (a & b) << 1
            a = (a^b) & mask
            b = carry & mask

        maxint = 0x7FFFFFFF
        if a <= maxint:
            return a

        return ~(a^mask)