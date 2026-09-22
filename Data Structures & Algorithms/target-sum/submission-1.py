class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = {}

        def dfs(i, remaining):
            if (i, remaining) in dp:
                return dp[(i, remaining)]

            if i == n and remaining == target:
                return 1

            if i == n:
                return 0

            res = 0
            num = nums[i]

            # add
            res += dfs(i+1, remaining + num)

            # substract
            res += dfs(i+1, remaining - num)

            dp[(i, remaining)] = res

            return dp[(i, remaining)]

        return dfs(0, 0)