class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2: return False

        target = total // 2

        def helper(value, i):
            nonlocal target
            
            if value == target: return True
            if i == len(nums) or value > target: return False

            one = helper(value + nums[i], i + 1)
            two = helper(value, i + 1)

            return one or two

        return helper(0,0)