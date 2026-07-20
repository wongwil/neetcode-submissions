class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftbounds = [-1] * n
        rightbounds = [n] * n

        stack = []
        for i in range(n):
            height = heights[i]

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            if stack:
                leftbounds[i] = stack[-1]

            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            height = heights[i]

            while stack and heights[stack[-1]] >= height:
                stack.pop()

            if stack:
                rightbounds[i] = stack[-1]

            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (1 + (rightbounds[i] - 1) - (leftbounds[i] + 1)))

        return res