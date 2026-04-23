class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)

        for x in numSet:
            if(x-1 not in numSet):
                length = 0
                while(x + length in numSet):
                    length += 1
                longest = max(longest,length)
        return longest
