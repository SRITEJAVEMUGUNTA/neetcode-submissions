class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        dp = defaultdict(int)
        def backtrack(num):
            if num > n:
                return
            if num == n:
                res[0] += 1
                return

            

            backtrack(num+1)
            backtrack(num+2)

        backtrack(0)
        return res[0]
        

            

            

        