class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def helper(value):
            if value > amount:
                return float("inf")
            if value == amount:
                return 0

            if value in dp:
                return dp[value]

            
            res = float("inf")
            for c in coins:
                res = min(res, 1 + helper(value+c))
            dp[value] = res
            return res
        
        res = helper(0)

        return res if res != float("inf") else - 1

        