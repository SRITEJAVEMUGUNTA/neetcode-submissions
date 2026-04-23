from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l, r = 0, 0
        while r < k:
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            r += 1
        res = []
        while r < len(nums) + 1:
            if q[0] < l:
                q.popleft()
            res.append(nums[q[0]])

            if r >= len(nums):
                break
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            l += 1
            r += 1

        return res