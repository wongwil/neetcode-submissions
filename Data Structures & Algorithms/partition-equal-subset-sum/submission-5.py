class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        n = len(nums)
        if total % 2 != 0:
            return False

        mem = {0 : True}

        def dfs(i, remaining):
            if remaining in mem:
                return mem[remaining]
                
            if i == n:
                return False

            # take
            if remaining >= nums[i] and dfs(i+1, remaining - nums[i]):
                mem[remaining] = True
                return True

            # skip
            if dfs(i+1, remaining):
                mem[remaining] = True
                return True

            mem[remaining] = False
            return False
        
        return dfs(0, total / 2)