class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def backtrack(idx, bought):
            if idx >= len(prices): return 0
            if (idx, bought) in dp: return dp[(idx, bought)]


            base = backtrack(idx + 1, bought)

            if bought:
                sell = backtrack(idx+2, not bought) + prices[idx]
                dp[(idx, bought)] = max(sell, base)
            else:
                buy = backtrack(idx+1, not bought) - prices[idx]
                dp[(idx, bought)] = max(buy, base)


            return dp[(idx, bought)]

        


        return backtrack(0, False)