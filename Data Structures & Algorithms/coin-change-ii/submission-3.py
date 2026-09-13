class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dic = {}
        def memo(idx, val):
            if idx == len(coins):
                if val == amount: return 1
                return 0
            
            if val > amount: return 0

            if val == amount: return 1

            if (idx, val) in dic: return dic[(idx,val)]


            dic[(idx,val)] = memo(idx + 1, val) + memo(idx, val + coins[idx])

            return dic[(idx,val)]

        return memo(0,0)
