class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(arr):
            rob1 = rob2 = 0

            for num in arr:
                temp = rob1 + num
                rob1 = rob2
                rob2 = max(temp, rob2)
            
            return rob2
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])
