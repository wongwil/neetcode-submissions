class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rightprod = [1] * n 
        leftprod = [1] * n

        rightprod[0] = nums[0]
        leftprod[-1] = nums[-1]
        for i in range(1, n, 1):
            rightprod[i] = rightprod[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            leftprod[i] = leftprod[i+1] * nums[i]

        res = [1] * n 
        for i in range(n):
            if i == 0:
                res[i] = leftprod[i+1]
            elif i == n-1:
                res[i] = rightprod[i-1]
            else:
                res[i] = leftprod[i+1] * rightprod[i-1]

        return res

