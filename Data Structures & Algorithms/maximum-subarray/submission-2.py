class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for x in nums:
            if(curSum < 0):
                curSum = 0
            curSum += x

            maxSub = max(maxSub, curSum)
        return maxSub
