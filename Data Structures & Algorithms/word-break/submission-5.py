class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def helper(idx):
            if idx == len(s):
                return True

            if idx in dp:
                return dp[idx]
            

            flag = False

            for word in wordDict:
                if s[idx:idx+len(word)] == word and helper(idx+len(word)):
                    flag = True
                    break
            dp[idx] = flag
            return flag

        return helper(0)
        

