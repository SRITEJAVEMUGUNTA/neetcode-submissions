class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def helper(num):
            if num == 0:
                return 0
            
            if num in dp:
                return dp[num]

            res = float("inf")

            for c in coins:
                if num - c >= 0:
                    res = min(res, 1+helper(num-c))
            dp[num] = res
            return res
        
        sol = helper(amount)
        return sol if sol != float("inf") else -1