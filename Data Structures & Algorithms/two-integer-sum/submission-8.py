class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}


        for i, num in enumerate(nums):
            last = target - num

            if last in dic:
                return[dic[last], i]
            
            if num not in dic:
                dic[num] = i
        

