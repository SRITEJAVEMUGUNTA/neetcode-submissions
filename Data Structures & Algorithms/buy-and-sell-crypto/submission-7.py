class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = float("inf")
        for p in prices:
            if p < low:
                low = p
            else:
                res = max(res, p-low)
        
        return res