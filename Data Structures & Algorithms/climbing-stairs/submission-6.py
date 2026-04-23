class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        dp = defaultdict(int)
        def backtrack(num):
            if num > n:
                return 0
            if num == n:
                return 1

            if num in dp:
                return dp[num]

            dp[num] += backtrack(num+1) + backtrack(num+2)

            return dp[num]

        return backtrack(0)
        

            

            

        