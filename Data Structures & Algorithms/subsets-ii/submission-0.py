class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        def helper(idx, arr):
            if idx == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[idx])
            helper(idx + 1, arr)
            arr.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 1
            helper(idx+1, arr)


        

        helper(0,[])

        return res