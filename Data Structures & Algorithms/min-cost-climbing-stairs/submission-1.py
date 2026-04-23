class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        '''
        Many Subproblems
        Start with the min of 0, 1 index

        from there find the min of the i + 1,  i + 2 index for each
        sub problem

        repeat

        return the value up till that point
        '''
        dp = {}

        def backtracking(idx):
            if(idx + 1 >= len(cost) or idx + 2 >= len(cost)):
                return cost[idx]
            if(idx in dp):
                return dp[idx]
            dp[idx] = cost[idx] + min(backtracking(idx+1), backtracking(idx+2))

            return dp[idx]


        return min(backtracking(0), backtracking(1))
        
    
    