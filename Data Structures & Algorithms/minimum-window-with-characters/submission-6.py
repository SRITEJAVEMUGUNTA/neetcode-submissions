from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_t = Counter(t)
        dic_s = defaultdict(int)
        l = 0
        match = 0
        count = float("inf")
        res = ""
        for r in range(len(s)):
            let = s[r]
            dic_s[let] += 1

            if dic_s[let] == dic_t[let]:
                match += 1
                
            
            while match == len(dic_t):
                
                if(r-l+1 < count):
                    count = r-l+1
                    res = s[l:r+1]
                letter_to_remove = s[l]

                dic_s[letter_to_remove] -= 1

                if dic_s[letter_to_remove] < dic_t[letter_to_remove]:
                    match -= 1
                

                l += 1

        return res