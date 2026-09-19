class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])

        return res