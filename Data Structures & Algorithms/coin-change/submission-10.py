class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = {}
        def helper(total):
            if total == amount:
                return 0

            if total in dp:
                return dp[total]
            res = float("inf")

            for c in coins:
                if total + c <= amount:
                    res = min(res, 1 + helper(total+c))

            dp[total] = res
            return res

        
        num = helper(0)
        return num if num != float("inf") else -1