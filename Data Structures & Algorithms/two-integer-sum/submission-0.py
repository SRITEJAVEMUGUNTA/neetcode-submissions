class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = ['x','x']
        for x in range(len(nums)):
            for i in range(x+1, len(nums)):
                if(nums[i] + nums[x] == target):
                    arr[0] = x
                    arr[1] = i
        return arr

                
        