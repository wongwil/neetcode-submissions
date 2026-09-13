class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [[-1] * 2 for i in range(n)]
        def dfs(i, b):
            if i > b:
                return 0

            if i == b:
                return nums[i]

            flag = b == n-2

            if mem[i][flag] != -1:
                return mem[i][flag]

            mem[i][flag] = max(dfs(i+1, b), dfs(i+2, b) + nums[i])

            return mem[i][flag]

        if n >= 2:
            return max(dfs(0, n-2), dfs(1, n-1))
        elif n == 0:
            return 0
        else:
            return nums[-1]