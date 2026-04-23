class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(start, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target:
                return


            for i in range(start, len(nums)):
                arr.append(nums[i])
                helper(i, arr, total + nums[i])
                arr.pop()
        


        helper(0, [], 0)

        return res