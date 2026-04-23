class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        one = len(text1)
        two = len(text2)
        dp = [[0 for _ in range(two + 1)]for i in range(one + 1)]
        for o in range(one-1,-1,-1):
            for t in range(two-1,-1,-1):
                if text1[o] == text2[t]:
                    dp[o][t] = 1 + dp[o+1][t+1]
                else:
                    dp[o][t] = max(dp[o+1][t], dp[o][t+1])
        return dp[0][0]
