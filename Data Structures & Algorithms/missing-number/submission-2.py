class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums) + 1

        for i in range(n):
            res ^= i

        for num in nums:
            res ^= num

        return res