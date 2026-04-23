class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        best = -1
        while l <= r:
            mid = l + (r-l)// 2
            val = 0

            for num in piles:
                val += math.ceil(float(num)/mid)

            
            if val <= h:
                best = mid
                r = mid -1
            else:
                l = mid + 1

        return best