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
            # If you reach the end or step beyond, the cost is 0 since no more steps are needed
            if idx >= len(cost):
                return 0
            if idx in dp:
                return dp[idx]
            
            # Recursively calculate the minimum cost of taking either 1 step or 2 steps
            dp[idx] = cost[idx] + min(backtracking(idx + 1), backtracking(idx + 2))
            return dp[idx]

        # You can either start at step 0 or step 1
        return min(backtracking(0), backtracking(1))
        
    
    