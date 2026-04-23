class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}
        def helper(idx, total):
            if total == 0:
                return 1
            
            if idx >= len(coins):
                return 0

            if (total, idx) in dp:
                return dp[(total,idx)]


            num = 0
            if total - coins[idx] >= 0:
                num += helper(idx, total - coins[idx])
            

            num += helper(idx+1, total)

            dp[(total, idx)] = num

            return num

        


        return helper(0, amount)