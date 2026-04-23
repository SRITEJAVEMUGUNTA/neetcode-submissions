class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,arr,total):
            if (target == total):
                res.append(arr.copy())
                return
            
            if target < total or i >= len(nums):
                return
            
            
            arr.append(nums[i])
            dfs(i, arr, total + nums[i])
            arr.pop()
            dfs(i + 1, arr, total)
        

        dfs(0, [], 0)

        return res