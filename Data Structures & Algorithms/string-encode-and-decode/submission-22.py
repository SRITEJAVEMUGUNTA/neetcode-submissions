class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for string in strs:
            res_str += "や" + string

        
        return res_str
    def decode(self, s: str) -> List[str]:
        if not s: return []
        idx = 0

        arr = []
        word = ""
        while idx < len(s):
            if(s[idx] == "や"):
                if(idx != 0): arr.append(word)
                idx += 1
                word = ""
                continue

            word += s[idx]
            idx += 1
        
    
        arr.append(word)

        return arr
            

