class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            
            res.append(str(len(string)))
            res.append("#")
            res.append(string)

        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        num = 0
        while i < len(s):
            j = i

            while j < len(s) and s[j].isdigit():
                j += 1
            
            num = int(s[i:j])

            i = j + 1
            j = i + num
            res.append(s[i:j])
            i = j

        return res
            