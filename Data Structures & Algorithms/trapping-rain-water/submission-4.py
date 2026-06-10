class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        leftmax = height[l]
        rightmax = height[r]

        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                res += max(0, leftmax - height[l])
                leftmax = max(height[l], leftmax)
            else:
                r -= 1
                res += max(0, rightmax - height[r])
                rightmax = max(height[r], rightmax)

        return res