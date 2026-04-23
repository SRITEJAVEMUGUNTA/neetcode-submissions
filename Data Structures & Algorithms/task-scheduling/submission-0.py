from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0
        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    cooldown.append([cnt, time+n])

            if cooldown and cooldown[0][1] <= time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        
        return time