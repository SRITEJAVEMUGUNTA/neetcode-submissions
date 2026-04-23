class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        lowest = prices[0]

        for x in prices:
            if x < lowest:
                lowest = x
            
            best = max(best, x-lowest)
        return best