class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0

        lowest = prices[0]

        for x in prices:
            if x < lowest:
                lowest = x
            sol = max(sol, x - lowest)

        return sol
            