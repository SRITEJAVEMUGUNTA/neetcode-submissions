class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = {}
        def helper(total):
            if total == 0:
                return 0

            if total in dp:
                return dp[total]
            res = float("inf")

            for c in coins:
                if total - c >= 0:
                    res = min(res, 1 + helper(total-c))

            dp[total] = res
            return res

        
        num = helper(amount)
        return num if num != float("inf") else -1