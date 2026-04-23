class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]

        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if (i+len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i+len(word)] = dp[i] or dp[i+len(word)]


        return dp[len(s)]