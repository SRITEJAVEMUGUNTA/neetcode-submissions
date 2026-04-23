class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        total_sum = 0
        res = float("-inf")
        for r in range(len(nums)):
            if total_sum < 0:
                print(total_sum)
                total_sum = 0

            total_sum += nums[r]

            res = max(res, total_sum)
        
        return res
