class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        pre = 1
        for i in range(n):
            prefix[i] = pre
            pre *= nums[i]

        suff = 1
        for i in range(n-1, -1, -1):
            suffix[i] = suff
            suff *= nums[i]

        res = [1] * n

        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res