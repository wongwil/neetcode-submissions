class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        n = len(nums)
        if total % 2 != 0:
            return False

        mem = {}

        def dfs(i, remaining):
            if remaining == 0:
                return True

            if (i, remaining) in mem:
                return mem[(i, remaining)]
                
            if i == n:
                return False

            # take
            if remaining >= nums[i] and dfs(i+1, remaining - nums[i]):
                mem[(i, remaining)] = True
                return True

            # skip
            if dfs(i+1, remaining):
                mem[(i, remaining)] = True
                return True

            mem[(i, remaining)] = False
            return False
        
        return dfs(0, total / 2)