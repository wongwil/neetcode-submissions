class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, subRes):
            res.append(subRes.copy())

            if i == len(nums):
                return

            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                subRes.append(nums[j])
                dfs(j+1, subRes)

                subRes.pop()


        dfs(0, [])

        return res