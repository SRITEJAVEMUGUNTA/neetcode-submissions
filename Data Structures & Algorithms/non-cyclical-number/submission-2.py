class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def changeNum(num):
            res = 0
            while num:
                res += (num %10) ** 2
                num //= 10


            return res
        while n != 1:
            n = changeNum(n)

            if n in seen:
                return False

            seen.add(n)

        return True