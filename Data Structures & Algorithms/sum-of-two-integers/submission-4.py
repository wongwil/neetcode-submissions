class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0

        # use a = a + b (without carry)
        # b = carry
        # everything within 32-bit masks
        # keep adding until there is no carry left

        mask = 0xFFFFFFFF
        while b != 0:
            sumWithoutCarry = a ^ b 
            carry = (a & b) << 1

            a = sumWithoutCarry & mask
            b = carry & mask

        maxint = 0x7FFFFFFF

        if a <= maxint:
            return a

        return ~(a^mask)