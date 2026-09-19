class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpmin = [0] * n
        dpmax = [0] * n

        dpmin[0] = nums[0]
        dpmax[0] = nums[0]
        maxseen = nums[0]

        for i in range(1, n):
            dpmax[i] = max(dpmax[i-1] * nums[i], dpmin[i-1] * nums[i], nums[i])
            maxseen = max(maxseen, dpmax[i])
            dpmin[i] = min(dpmax[i-1] * nums[i], dpmin[i-1] * nums[i], nums[i])

        return maxseen