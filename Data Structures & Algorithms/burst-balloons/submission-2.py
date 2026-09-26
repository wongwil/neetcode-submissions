class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def dfs(l, r):
            if r < l:
                return 0

            if (l,r) in dp:
                return dp[(l,r)]

            # choosing i in (l, r) as the last one
            res = 0
            for i in range(l, r + 1):
                coins = dfs(l, i-1) # choose j in (l, i-1)
                coins += dfs(i+1, r) # choose j in (i+1, r)
                coins += nums[l-1] * nums[i] * nums[r+1] # choose the last one
                res = max(res, coins)
            
            dp[(l,r)] = res
            return dp[(l,r)]


        nums = [1] + nums + [1]

        return dfs(1, len(nums) - 2)