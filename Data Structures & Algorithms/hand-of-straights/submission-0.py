import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        dic = Counter(hand)
        minH = list(dic.keys())

        heapq.heapify(minH)

        while minH:
            num = minH[0]
            

            for i in range(num, num + groupSize):
                if dic[i] <= 0:
                    return False
                
                dic[i] -= 1

                if dic[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True