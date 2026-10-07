class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n:
            if n & 1:
                res |= (1 << 31 - i)
            i += 1
            n = n >> 1
        return res