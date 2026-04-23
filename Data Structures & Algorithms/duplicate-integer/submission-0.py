class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for x in nums:
            if(x in d.keys()):
                d[x] += 1
            else:
                d[x] = 1
    
        for i in d.values():
            if(i > 1):
                return True
        return False    