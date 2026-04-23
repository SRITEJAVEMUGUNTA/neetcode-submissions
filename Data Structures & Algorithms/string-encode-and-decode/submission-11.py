class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            inner = ""
            strNum = ""
            while s[i] != "#":
                strNum += s[i]
                i += 1
            num = int(strNum)
            print(num)
            inner = s[i+1: i+1+num]
            i = i+1+num
            res.append(inner)
            print(res)
        return res
