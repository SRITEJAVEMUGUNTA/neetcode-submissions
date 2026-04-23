class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for x in strs:
            res += str(len(x)) + "@" + x
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        

        while i < len(s):
            r = i
            
            while s[r] != "@":
                r += 1
            length = int(s[i:r])

            res.append(s[r+1:r+1+length])

            i = r+1+length
        
        return res
