class Solution:

    def encode(self, strs: List[str]) -> str:
        res  = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res
    def decode(self, s: str) -> List[str]:
        res = []


        l = r = 0

        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            
            wrdLen = int(s[l:r])

            l = r + 1
            r = l + wrdLen

            res.append(s[l:r])

            l = r
        return res
            



