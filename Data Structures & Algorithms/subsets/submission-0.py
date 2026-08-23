class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return

            dfs(i + 1, sub) # not include X
            sub.append(nums[i])
            dfs(i+1, sub) # include X
            sub.pop() # pop X for the previous branch

        dfs(0, [])

        return res
