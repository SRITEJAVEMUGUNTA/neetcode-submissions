class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        memo = {}

        def dfs(curr):
            if curr > n:
                return 0
            
            if curr == n:
                return 1

            memo[curr] = dfs(curr+1) + dfs(curr+2)
            return memo[curr]
        
        return dfs(0)
            