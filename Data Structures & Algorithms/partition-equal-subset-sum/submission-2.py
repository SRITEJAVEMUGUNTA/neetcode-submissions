class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dic = {}
        def helper(idx, one, two):
            if idx == len(nums):
                if one == two:
                    
                    return True
                return False

            
            uno = helper(idx+1, one + nums[idx], two)
            dos = helper(idx+1, one, two + nums[idx])

            return uno or dos

        return helper(0, 0, 0)

