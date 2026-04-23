class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)

        count = 0

        for num in nums:
            if num-1 not in mySet:
                inner = 1
                num +=1
                while num in mySet:
                    inner += 1
                    num += 1
                
                count = max(count, inner)
        
        return count
