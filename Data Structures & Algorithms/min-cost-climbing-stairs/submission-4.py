class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float("inf") for _ in range(len(cost) + 1)]

        dp[-1] = 0


        for i in range(len(cost) - 1, -1, -1):
            print(dp)
            if i + 2 <= len(cost):
                dp[i] = cost[i] + min(dp[i+2], dp[i+1])
            else:
                dp[i] = cost[i] + dp[i+1]

        return min(dp[0], dp[1])
