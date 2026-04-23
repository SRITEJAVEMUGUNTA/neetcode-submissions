class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)

        for i, (x,y) in enumerate(points):
            num = math.sqrt((x**2) + (y**2))
            print(max_heap)
            if len(max_heap) < k:
                heapq.heappush(max_heap, [-num, i])
                continue
            if num < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, [-num, i])

        res = []
        for _, i in max_heap:
            res.append(points[i])
        
        return res

        

            
        


        print(max_heap)
        return max_heap