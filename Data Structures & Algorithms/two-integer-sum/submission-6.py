class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for x in range(len(nums)):
            dic[nums[x]] = x
        
        for i in range(len(nums)):
            sol = target - nums[i]

            if sol in dic:
                if(i != dic[sol]):
                    return([i, dic[sol]])