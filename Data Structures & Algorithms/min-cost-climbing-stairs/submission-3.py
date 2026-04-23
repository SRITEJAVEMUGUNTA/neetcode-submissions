class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def backtrack(idx):
            if idx >= len(cost):
                return 0
            if idx in dp:
                return dp[idx]


            res = cost[idx] + min(backtrack(idx+1), backtrack(idx+2))

            dp[idx] = res
            return res
        


        return min(backtrack(0), backtrack(1))