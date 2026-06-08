class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)

        res = 0
        for n in nums:
            if n-1 not in myset:
                # we found the tail of the sequence
                length = 1
                while n + length in myset:
                    length += 1
                res = max(res, length)


        return res