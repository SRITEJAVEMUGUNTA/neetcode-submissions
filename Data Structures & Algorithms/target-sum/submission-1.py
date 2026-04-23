class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def helper(total, idx):
            if idx == len(nums) and total == target:
                return 1
            
            if idx >= len(nums):
                return 0

            if (total, idx) in dp:
                return dp[(total, idx)]
            

            one = helper(total+nums[idx], idx+1)
            two = helper(total-nums[idx], idx+1)

            dp[(total, idx)] = one + two
            return one + two
        

        return helper(0, 0)
        