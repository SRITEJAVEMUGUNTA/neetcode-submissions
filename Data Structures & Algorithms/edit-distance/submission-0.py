class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lenOne = len(word1)
        lenTwo = len(word2)
        
        dp = [[0 for _ in range(lenTwo + 1)] for i in range(lenOne + 1)]

        for i in range(lenOne+1):
            dp[i][lenTwo] = lenOne - i
        for i in range(lenTwo+1):
            dp[lenOne][i] = lenTwo - i

        for i in range(lenOne-1, -1, -1):
            for j in range(lenTwo-1, -1, -1):
                if(word1[i] == word2[j]):
                    dp[i][j] = dp[i+1][j+1]
                    continue

                # Insert case
                ins = 1 + dp[i+1][j]

                # Delete Case
                delete = 1 + dp[i][j+1]

                # Replace
                rep = 1 + dp[i+1][j+1]

                dp[i][j] = min(ins, delete, rep)

        print(dp)
        return dp[0][0]