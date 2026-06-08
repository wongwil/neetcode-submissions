class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)

        res = 0
        for n in nums:
            if n-1 not in myset:
                # we found the tail of the sequence
                tempres = 1
                res = max(tempres,res)
                curr = n
                while curr + 1 in myset:
                    tempres += 1
                    res = max(tempres, res)
                    curr += 1


        return res