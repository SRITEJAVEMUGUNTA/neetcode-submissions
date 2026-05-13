class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest= 0
        for num in nums:
            if num - 1 in mySet:
                continue
            
            inner = 1
            while True:
                if num + inner in mySet:
                    inner += 1
                else:
                    break
                
            longest = max(longest, inner)
    
        return longest