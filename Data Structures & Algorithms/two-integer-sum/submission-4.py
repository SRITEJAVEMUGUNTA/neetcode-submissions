class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for x in range(len(nums)):
            dic[nums[x]] = x
        
        for i in range(len(nums)):
            comp = target - nums[i]

            if(comp in dic and dic[comp] != i):
                if(dic[comp] < i):
                    return([dic[comp], i])
                else:
                    return([i, dic[comp]])
                