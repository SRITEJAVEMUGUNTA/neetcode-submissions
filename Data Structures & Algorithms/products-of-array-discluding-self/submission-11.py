class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]

        running_product = 1

        for i in range(len(nums)):
            prefix[i] = running_product
            running_product *= nums[i]

        running_product = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= running_product
            running_product *= nums[i]
        return prefix