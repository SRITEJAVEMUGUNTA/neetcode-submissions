class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        res = 0
        for i in range(len(prices)):
            stock = prices[i]
            if stock < low:
                low = stock
            else:
                res = max(res, stock-low)

        return res