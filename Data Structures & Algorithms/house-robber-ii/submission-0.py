class Solution:
    def rob(self, nums: List[int]) -> int:

        

        def help(arr):

            rob1 = rob2 = 0

            #[rob1,rob2,n,n+1,end]
            for n in arr:
                temp = max(rob1+n, rob2)
                rob1 = rob2

                rob2 = temp

            return rob2
        
        return max(nums[0], help(nums[1:]), help(nums[:-1]))