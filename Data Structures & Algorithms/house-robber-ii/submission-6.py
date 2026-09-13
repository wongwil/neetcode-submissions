class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        
        def dfs(i, b):
            if i > b:
                return 0
            if i == b:
                return nums[i]
            if mem[i] != -1:
                return mem[i]
            mem[i] = max(dfs(i+1, b), dfs(i+2, b) + nums[i])
            return mem[i]

        mem = [-1] * n
        a = dfs(0, n-2)
        mem = [-1] * n 
        x = dfs(1, n-1)

        return max(a,x)