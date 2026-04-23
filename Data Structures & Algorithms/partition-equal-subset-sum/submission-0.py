class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def helper(idx, arr1, arr2):
            if idx == len(nums):
                if sum(arr1) == sum(arr2):
                    return True
                return False
            

            arr1.append(nums[idx])
            one = helper(idx+1, arr1, arr2)
            arr1.pop()
            arr2.append(nums[idx])
            two = helper(idx+1, arr1, arr2)
            arr2.pop()

            return one or two

        return helper(0, [], [])

