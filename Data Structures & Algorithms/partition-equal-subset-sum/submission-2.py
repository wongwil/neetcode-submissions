class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return False
        
        mem = {}
        def dfs(i, remainder):
            if remainder in mem:
                return mem[remainder]

            if remainder == 0:
                return True

            if i >= n:
                return False

            if remainder >= nums[i]  and dfs(i+1, remainder - nums[i]):
                mem[remainder] = True
                return True
            
            if dfs(i+1, remainder):
                mem[remainder] = True
                return True

            mem[remainder] = False
            return False
            
            
            
        return dfs(0, total / 2)