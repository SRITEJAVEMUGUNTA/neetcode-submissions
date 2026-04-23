class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for i in range(m)]

        def helper(r,c):
            if r == m - 1 and c == n-1:
                return 1
                        
            if r >= m or c >= n:
                return 0

            if dp[r][c] != 0:
                return dp[r][c]
            total = helper(r+1,c) + helper(r,c+1)
            dp[r][c] = total
            return total

        

        return helper(0,0)