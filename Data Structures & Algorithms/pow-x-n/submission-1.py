class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def findPow(num, exp):
            if num == 0:
                return 0
            
            if exp == 0:
                return 1

            res = findPow(num, exp // 2)
            res *= res

            return res * num if exp % 2 == 1 else res

        

        num = findPow(x, abs(n))

        return num if n >= 0 else 1/num