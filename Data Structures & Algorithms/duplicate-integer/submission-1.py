class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)

        for x in dic.values():
            if(x > 1):
                return True
        return False