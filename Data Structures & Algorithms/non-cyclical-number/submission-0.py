class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def changeNum(num):
            strNum = str(num)
            res = 0
            for char in strNum:
                res += int(char) ** 2

            return res
        while n != 1:
            n = changeNum(n)

            if n in seen:
                return False

            seen.add(n)

        return True