class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}
        def dfs(idx):
            if idx == len(nums)-1:
                return 0

            if nums[idx] == 0:
                return float("inf")

            if idx in memo:
                return memo[idx]


            innerRes = float("inf")
            distance = nums[idx]

            for j in range(1, distance+1):
                if idx + j < len(nums):
                    innerRes = min(innerRes, 1 + dfs(idx+j))

            memo[idx] = innerRes
            return innerRes

        return dfs(0)