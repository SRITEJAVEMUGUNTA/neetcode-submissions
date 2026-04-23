class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                arr = subsets[i]
                subsets.append(arr+[num])

        return subsets