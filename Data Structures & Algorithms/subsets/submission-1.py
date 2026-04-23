class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]


        for num in nums:
            for i in range(len(arr)):
                sub = arr[i]
                arr.append(sub + [num])

        return arr