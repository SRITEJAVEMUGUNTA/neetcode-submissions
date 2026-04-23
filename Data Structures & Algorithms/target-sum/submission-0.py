class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]

        def helper(total, idx):
            if idx == len(nums) and total == target:
                res[0] += 1
                return
            
            if idx >= len(nums):
                return
            

            helper(total+nums[idx], idx+1)
            helper(total-nums[idx], idx+1)
        

        helper(0, 0)
        return res[0]