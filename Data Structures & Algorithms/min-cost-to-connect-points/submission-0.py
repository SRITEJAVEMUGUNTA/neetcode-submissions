import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dic = defaultdict(list)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                val = abs(x1-x2) + abs(y1-y2)
                dic[i].append((val, j))
                dic[j].append((val, i))

        

        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap,(0,0))
        res = 0
        visited = set()
        while min_heap:
            val, idx = heapq.heappop(min_heap)

            if idx in visited:
                continue

            visited.add(idx)
            res += val
            if len(visited) == len(points):
                return res
            
            for v, nei in dic[idx]:
                if nei not in visited:
                    heapq.heappush(min_heap, (v, nei))

        return res
