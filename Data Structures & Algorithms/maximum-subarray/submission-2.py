class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        res = curr
        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res  = max(res, curr)


        return res