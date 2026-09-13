class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1] * n

        def dfs(i):
            # dfs(i) := #ways to reach n
            if i == n:
                return 1
            elif i > n:
                return 0
            
            if mem[i] != -1:
                return mem[i]

            mem[i] = dfs(i + 1) + dfs(i + 2)
            return mem[i]

        return dfs(0)