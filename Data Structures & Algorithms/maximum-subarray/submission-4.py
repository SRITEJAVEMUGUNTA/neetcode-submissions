class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curTotal = 0
        for r in range(len(nums)):
            if curTotal < 0:
                curTotal = 0
            
            curTotal += nums[r]

            res = max(res,curTotal)

        return res
        
