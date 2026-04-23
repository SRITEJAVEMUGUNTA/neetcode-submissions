class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def helper(idx, buying):
            if idx >= len(prices):
                return 0
            if (idx, buying) in dp:
                return dp[(idx, buying)]
            cooldown = helper(idx+1, buying)
            if buying:
                buyPower = helper(idx+1, not buying) - prices[idx]
                dp[(idx, buying)] = max(cooldown, buyPower)
                return dp[(idx, buying)]
            else:
                sellPower = helper(idx+2, not buying) + prices[idx]
                dp[(idx, buying)] = max(cooldown, sellPower)
                return dp[(idx, buying)]
        


        return helper(0, True)