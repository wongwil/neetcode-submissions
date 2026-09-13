class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    # run once for nums = [0, n-2]
    # once for nums= [1, n-1]
    def helper(self, nums):
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [-1] * n

        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]

