from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter_s = Counter(s)
        counter_t = Counter(t)

        if len(counter_s) != len(counter_t): return False

        for key in counter_s:
            if key not in counter_t or counter_s[key] != counter_t[key]:
                return False

        


        return True
            
            