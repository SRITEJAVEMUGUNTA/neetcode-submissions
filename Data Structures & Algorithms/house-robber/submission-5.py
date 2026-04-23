class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def backtrack(idx):
            if idx >= len(nums):
                return 0

            if idx in dp:
                return dp[idx]

            res = max(nums[idx] + backtrack(idx+2), backtrack(idx+1))
            dp[idx] = res
            return dp[idx]

        
        return backtrack(0)