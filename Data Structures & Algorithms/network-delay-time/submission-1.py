import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)

        dic = defaultdict(list)

        for start, end, time in times:
            dic[start].append((time,end))

        heapq.heappush(min_heap, (0,k))
        time_taken = 0
        visited = set()
        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                print(node)
                continue

            visited.add(node)
            time_taken = max(time_taken, time)
            
            if len(visited) == n:
                return time_taken
            
            for t, nei in dic[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + t, nei))

        return time_taken if len(visited) == n else -1

        



        
