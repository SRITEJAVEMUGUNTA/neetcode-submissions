class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]

        for r in range(m-2,-1,-1):
            newRow = [1 for _ in range(n)]
            for c in range(n-2,-1,-1):
                newRow[c] = newRow[c+1] + dp[c]
            dp = newRow
        return dp[0]