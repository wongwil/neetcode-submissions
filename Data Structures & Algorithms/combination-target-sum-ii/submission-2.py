class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, subRes, total):      
            if total == target:
                res.append(subRes.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue # skip because that's the same element 

                if total + candidates[j] > target:
                    break # stop looping because we are above the target

                subRes.append(candidates[j])
                dfs(j+1, subRes, total + candidates[j])
                subRes.pop()
            

        dfs(0, [], 0)

        return res