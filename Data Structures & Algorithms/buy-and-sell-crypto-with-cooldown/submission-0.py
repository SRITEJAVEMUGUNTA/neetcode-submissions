class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def helper(idx, buying):
            if idx >= len(prices):
                return 0
            
            cooldown = helper(idx+1, buying)
            if buying:
                buyPower = helper(idx+1, not buying) - prices[idx]
                return max(cooldown, buyPower)
            else:
                sellPower = helper(idx+2, not buying) + prices[idx]
                return max(cooldown, sellPower)
        


        return helper(0, True)