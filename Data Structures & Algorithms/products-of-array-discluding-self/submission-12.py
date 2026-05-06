class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1 for _ in range(len(nums))]
        running_prod = 1

        for i, num in enumerate(nums):
            arr[i] = running_prod
            running_prod *= num

        running_prod = 1

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            arr[i] *= running_prod
            running_prod *= num


        return arr
    