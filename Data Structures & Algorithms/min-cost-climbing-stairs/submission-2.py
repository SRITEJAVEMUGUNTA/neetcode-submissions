class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        def backtrack(idx):
            if idx >= len(cost):
                return 0
            res = cost[idx] + min(backtrack(idx+1), backtrack(idx+2))
            return res
        


        return min(backtrack(0), backtrack(1))