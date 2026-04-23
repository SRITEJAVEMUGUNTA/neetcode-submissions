class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for c in coins:
            for num in range(amount+1):
                if c <= num:
                    dp[num] += dp[num-c]
        
        return dp[amount]