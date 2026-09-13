class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            if mem[i] != -1:
                return mem[i]
            mem[i] = max(dfs(i+2), dfs(i+3)) + nums[i]
            return mem[i]

        return max(dfs(0), dfs(1))
            