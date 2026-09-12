class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dic = {}
        def backtrack(idx, val):
            if idx == len(nums):
                if val == target:
                    return 1
                return 0

            if (idx, val) in dic:
                return dic[(idx, val)]
            
            
            dic[(idx,val)] = backtrack(idx+1, val + nums[idx]) + backtrack(idx+1, val - nums[idx])

            return dic[(idx,val)]
            
        return backtrack(0,0)

        
