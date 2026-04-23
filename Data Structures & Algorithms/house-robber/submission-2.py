class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}

        def backtracking(idx):
            if idx >= len(nums):
                return 0
            if(idx in dp):
                return dp[idx]

            
            dp[idx] =max(nums[idx] + backtracking(idx + 2), backtracking(idx + 1))

            return dp[idx]

        
        return max(backtracking(1), backtracking(0))

