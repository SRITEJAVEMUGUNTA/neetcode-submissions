class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        mySet = set(nums)

        for num in mySet:
            
            inner = 0
            if num - 1 not in mySet:
                inner += 1
                while num + inner in mySet:
                    inner += 1

            res = max(res,inner)

        return res
