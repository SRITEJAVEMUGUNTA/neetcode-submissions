class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        l, r = 1, upperBound
        res = -1

        while l <= r:

            mid = (l+r) // 2

            total = 0

            for pile in piles:
                total += math.ceil(float(pile)/mid)

            if total <= h:
                res = mid
                r = mid - 1
            elif total > h:
                l = mid + 1

        
        return res