class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        dp = [False for _ in range(len(nums))]

        dp[0] = True

        for i in range(len(nums)-1):
            if dp[i]:
                distance = min(len(nums), i + nums[i] + 1)
                for j in range(i+1, distance):
                    dp[j] = True

        return dp[-1] 