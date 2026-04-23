class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        wata = 0

        while l < r:
            if heights[l] < heights[r]:
                num = heights[l] * (r-l)
                wata = max(num, wata)
                l += 1
            else:
                num = heights[r] * (r-l)
                wata = max(num, wata)
                r -= 1
            if wata == 41:
                print(l)
                print(r)
        return wata
