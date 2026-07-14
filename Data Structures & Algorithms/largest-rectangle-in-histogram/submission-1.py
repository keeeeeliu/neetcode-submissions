class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # min_height = min(heights)
        # res = min_height * len(heights)
        # stack = []
        # for i, h in enumerate(heights):
        #     if h > res:
        #         res = h
        #     curr_min = h
        #     for x in range(i + 1, len(heights)):
        #         curr_min = min(curr_min, heights[x])
        #         res = max(res, curr_min * (x - i + 1))
        n = len(heights)
        leftmost = [-1] * n
        rightmost = [n] * n 
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
                #left most is the shorter bar
            if stack:
                leftmost[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
                #right most is the shorter bar
            if stack:
                rightmost[i] = stack[-1]
            stack.append(i)

        maxArea = 0

        for i in range(n):
            left = leftmost[i] + 1
            right = rightmost[i] - 1
            maxArea = max((right - left + 1) * heights[i], maxArea)
        return maxArea