class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        best = [0]

        def backtrack(idx, prev, length):
            if idx == len(nums):
                best[0] = max(best[0], length)
                return

            if prev < nums[idx]:
                backtrack(idx+1,nums[idx], length + 1)

            backtrack(idx+1, prev, length)


            

        backtrack(0, float("-inf"), 0)

        return best[0]