class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {len(nums) - 1 : True}
        def dfs(i): # can i reach the end given i
            if i in dp:
                return dp[i]

            dp[i] = False
            for j in range(nums[i]+1):
                if j > 0 and dfs(i+j):
                    dp[i] = True
                    return dp[i]

            return dp[i]

        return dfs(0)
