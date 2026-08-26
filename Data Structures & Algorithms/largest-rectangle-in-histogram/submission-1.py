class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            idx = i
            while stack and height <= stack[-1][1]:
                ix, h = stack.pop()
                idx = ix
                res = max(res, h * (i-ix))
            stack.append([idx, height])


        
        lenHeights = len(heights)

        for idx, height in stack:
            res = max(res, height * (lenHeights - idx))

        return res
        
                

        