class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            sumWithoutCarry = a ^ b

            carry = (a & b) << 1

            a = sumWithoutCarry & mask
            b = carry & mask

        maxint = 0x7FFFFFFF
        if a <= maxint:
            return a

        return ~(a^mask)