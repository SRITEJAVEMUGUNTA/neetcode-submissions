class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def helper(arr, idx, total):
            if total == target:
                res.append(arr.copy())
                return

            if idx == len(nums): return
            
            if total > target: return

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                helper(arr, i, total + nums[i])
                arr.pop()

        helper([], 0, 0)

        return res