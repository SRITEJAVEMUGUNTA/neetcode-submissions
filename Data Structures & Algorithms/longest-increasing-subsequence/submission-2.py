class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [float("-inf")]

        def helper(idx, arr):
            res[0] = max(res[0], len(arr))
                        
            for i in range(idx, len(nums)):
                if not arr or arr[-1] < nums[i]:
                    arr.append(nums[i])
                    helper(i + 1, arr)
                    arr.pop()
            
            
        

        helper(0, [])
        return res[0]