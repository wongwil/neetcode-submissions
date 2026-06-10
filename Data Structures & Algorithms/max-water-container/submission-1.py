class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            res = max(res, self.calcArea(heights[l], heights[r], r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return res 
    def calcArea(self, lheight, rheight, length):
        return min(lheight, rheight) * length