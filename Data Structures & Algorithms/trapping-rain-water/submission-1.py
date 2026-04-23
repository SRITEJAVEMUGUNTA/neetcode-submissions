class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        heightL, heightR = height[l], height[r]
        res = 0
        while l < r:
            if heightL < heightR:
                l += 1
                heightL = max(heightL, height[l])
                res += heightL - height[l]
            else:
                r -= 1
                heightR = max(heightR, height[r])
                res += heightR - height[r]

            
        return res

