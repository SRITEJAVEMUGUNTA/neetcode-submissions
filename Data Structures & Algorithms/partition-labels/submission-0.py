from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = Counter(s)
        res = []
        l, r = 0, 0
        seen = set()
        while r < len(s):
            char = s[r]
            seen.add(char)
            dic[char] -= 1

            if dic[char] == 0:
                seen.remove(char)
            
            if not seen:
                res.append(r-l+1)
                l = r + 1
            r += 1
        
        return res


            