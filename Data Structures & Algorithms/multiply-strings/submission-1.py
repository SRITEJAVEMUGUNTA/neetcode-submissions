class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"
        res = [0 for i in range(len(num1) + len(num2))]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                num = int(num1[i1]) * int(num2[i2])

                res[i1+i2] += num
                res[i1+i2+1] += res[i1+i2] // 10
                res[i1+i2] = res[i1+i2] % 10

        res = res[::-1]
        zeroIdx = 0

        while zeroIdx < len(res) and res[zeroIdx] == 0:
            zeroIdx += 1
        
        res = map(str, res[zeroIdx:])

        return "".join(res)
            
                
