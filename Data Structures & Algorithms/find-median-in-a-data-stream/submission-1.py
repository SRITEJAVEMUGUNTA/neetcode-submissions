class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        #check for difference in value
        if(self.small and self.large and (self.small[0] * -1) > self.large[0]):
            heapq.heappush(self.large, (heapq.heappop(self.small) * -1))
        
        if(len(self.small) + 1 < len(self.large)):
            heapq.heappush(self.small, (heapq.heappop(self.large) * -1))
        elif(len(self.small) > len(self.large) + 1):
            heapq.heappush(self.large, (heapq.heappop(self.small) * -1))
        

    def findMedian(self) -> float:
        if(len(self.large) > len(self.small)):
            return self.large[0]
        elif(len(self.large) < len(self.small)):
            return self.small[0] * -1
        else:
            return ((self.small[0] * -1) + self.large[0])/2
        