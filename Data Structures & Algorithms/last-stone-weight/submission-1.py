import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-num for num in stones]

        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            if len(max_heap) == 0:
                return 0

            one = -heapq.heappop(max_heap)
            two = -heapq.heappop(max_heap)

            if one > two:
                heapq.heappush(max_heap, -(one-two))
            elif two > one:
                heapq.heappush(max_heap, -(two-one))


        return -max_heap[0] if max_heap else 0
