class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        
        for x in nums:
            if(x-1 not in nums):
                length = 0
                while(x+length in nums):
                    length += 1
                
                best = max(best, length)
        return best