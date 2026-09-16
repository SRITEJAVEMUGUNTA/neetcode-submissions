class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        count = 0
        while l < r:
            mid = (r+l) // 2
            print(nums[mid])
            if nums[mid] <= nums[r]:
                r = mid
            elif nums[mid] >= nums[l]:
                l = mid + 1
            
        return nums[l]