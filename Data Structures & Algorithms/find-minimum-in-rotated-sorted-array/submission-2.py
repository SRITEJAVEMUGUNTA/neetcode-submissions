class Solution:
    def findMin(self, nums: List[int]) -> int:
        beg = 0
        end = len(nums) - 1
        best = nums[0]

        while beg <= end:

            if(nums[beg] < nums[end]):
                best = min(best, nums[beg])
                break
            mid = (beg + end)//2

            best = min(best, nums[mid])

            if(nums[mid] >= nums[beg]):
                beg = mid + 1
            else:
                end = mid - 1
        return best



