class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def backtracking(num):
            if(num > n):
                return 0
            if(num == n):
                return 1
            if(num in dp):
                return dp[num]

            
            dp[num] = backtracking(num + 2) + backtracking(num + 1)

            return dp[num]
        
        return backtracking(0)