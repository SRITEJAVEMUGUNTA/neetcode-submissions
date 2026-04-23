class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for x in numSet:
            if(x-1 not in numSet):
                length = 0
                while(x+length in numSet):
                    length += 1
                
                res = max(res,length)
        return res
