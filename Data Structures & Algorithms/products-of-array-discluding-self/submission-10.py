class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = ["*"] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            
            prefix[i] = prefix[i-1] * nums[i-1]
        
        
        postFix = ["*"] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                postFix[-1] = 1
                continue
            
            postFix[i] = postFix[i+1] * nums[i+1]
            

        

        res = []
        print(prefix)
        print(postFix)
        for i in range(len(prefix)):
            res.append(prefix[i] *postFix[i])
        return res