class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]

        dp[0] = 0

        for i in range(len(nums)-1):
            if nums[i] <= 0:
                continue
            distance = nums[i]

            for j in range(1, distance + 1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], 1+dp[i])

        return dp[-1]
