class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        dp = [False for _ in range(len(nums))]

        dp[0] = True

        for i in range(len(nums)-1):
            if dp[i]:
                distance = nums[i]
                for j in range(1, distance + 1):
                    if i + j < len(nums):
                        dp[i+j] = True

        return dp[-1] 