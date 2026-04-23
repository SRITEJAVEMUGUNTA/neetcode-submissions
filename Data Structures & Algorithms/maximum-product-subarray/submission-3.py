class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            temp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMin * n, temp * n, n)
            
            res = max(res, curMax)
        return res

        