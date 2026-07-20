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
            r = rightbounds[i] - 1
            l = leftbounds[i] + 1

            width = r - l + 1 # l = 0, r = 2 => the width is 3

            res = max(res, width * heights[i])

        return res

