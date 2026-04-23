

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)

        postfix = 1
        for x in range(len(nums)-1,-1,-1):
            sol[x] = postfix

            postfix *= nums[x]

        prefix = 1
        for x in range(len(nums)):
            sol[x] *= prefix

            prefix *= nums[x]
        
        

        return sol

