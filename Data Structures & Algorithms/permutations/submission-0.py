class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def helper(arr, idx):
            if idx == len(nums):
                res.append(arr.copy())
                return
            

            for i in range(idx, len(arr)):
                arr[i], arr[idx] = arr[idx], arr[i]
                helper(arr,idx+1)
                arr[i], arr[idx] = arr[idx], arr[i]
        

        helper(nums, 0)

        return res