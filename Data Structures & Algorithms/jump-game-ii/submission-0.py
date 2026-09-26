class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {len(nums) - 1 : 0}
        def dfs(i):
            if i in dp:
                return dp[i]

            best = float("Inf")

            for j in range(nums[i] + 1):
                if j > 0 and i + j < len(nums):
                    best = min(best, 1 + dfs(i + j))
            
            dp[i] = best
            return dp[i]

        return dfs(0)
            