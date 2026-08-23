class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(i, subRes):
            if i == len(nums):
                res.append(subRes.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]

                subRes.append(nums[i])
                dfs(i+1, subRes)

                nums[i], nums[j] = nums[j], nums[i] # swap them back
                subRes.pop()

        dfs(0, [])

        return res