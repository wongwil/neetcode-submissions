class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        if n == 1:
            return nums[0]

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


        return max(dfs(0, n-2), dfs(1, n-1))