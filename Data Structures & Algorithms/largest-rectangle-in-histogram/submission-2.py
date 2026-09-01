class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = float("-inf")

        for i, val in enumerate(heights):
            index = i
            while stack and val <= stack[-1][1]:
                idx, v = stack.pop()
                index = idx
                res = max(res, v * (i - idx))
            
            stack.append([index, val])

        l = len(heights)
        for i, val in stack:
            res = max(res, val * (l - i))

        return res

        


