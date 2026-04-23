import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]

        max_heap = []
        heapq.heapify(max_heap)

        l, r = 0, 0

        while r < k - 1:
            heapq.heappush(max_heap, [-nums[r], r])
            r += 1
        res = []
        while r < len(nums):
            while max_heap and max_heap[0][1] < l:
                heapq.heappop(max_heap)
            

            heapq.heappush(max_heap, [-nums[r], r])
            res.append(-max_heap[0][0])

            r += 1
            l += 1

        return res


        