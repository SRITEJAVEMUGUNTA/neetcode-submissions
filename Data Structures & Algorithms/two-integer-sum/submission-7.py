class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            sol = target - nums[i]

            if sol in dic:
                return [dic[sol], i]
            
            dic[nums[i]] = i