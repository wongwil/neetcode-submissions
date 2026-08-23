class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subRes, currentSum):
            if i == len(nums):
                return

            if currentSum > target:
                return

            if currentSum == target:
                res.append(subRes.copy())
                return

            
            dfs(i+1, subRes, currentSum)

            subRes.append(nums[i])
            dfs(i, subRes, currentSum + nums[i])
            subRes.pop()

        
        dfs(0, [], 0)

        return res