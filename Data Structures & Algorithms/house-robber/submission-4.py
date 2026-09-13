class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if mem[i] != -1:
                return mem[i]
            mem[i] = max(dfs(i+1), dfs(i+2) + nums[i])
            return mem[i]

        return dfs(0)
            