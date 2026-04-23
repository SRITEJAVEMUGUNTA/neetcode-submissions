class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2: return False

        target = total // 2
        dp = {}
        def helper(value, i):
            if value == target: return True
            if (value, i) in dp: return dp[(value, i)]
            if value > target or i >= len(nums): return False

            one = helper(value + nums[i], i + 1)
            two = helper(value, i + 1)

            dp[(value, i)] = one or two

            return dp[(value, i)]

        return helper(0,0)