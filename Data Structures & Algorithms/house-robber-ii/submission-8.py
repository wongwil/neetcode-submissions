class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        mem = [[-1 for i in range(2)] for i in range(n)] 
        def dfs(i, b, flag):
            if i > b:
                return 0
            if i == b:
                return nums[i]
            if mem[i][flag] != -1:
                return mem[i][flag]
            mem[i][flag] = max(dfs(i+1, b, flag), dfs(i+2, b, flag) + nums[i])
            return mem[i][flag]

        a = dfs(0, n-2, 0)
        x = dfs(1, n-1, 1)

        return max(a,x)