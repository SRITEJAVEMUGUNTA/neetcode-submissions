class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        for x in nums:
            temp = rob1 + x
            rob1 = rob2

            rob2 = max(temp, rob2)

        return rob2