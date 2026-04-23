from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""

        res = [-1,-1]
        resLen = float("inf")
        
        target = Counter(t)

        have, need = 0, len(target)
        window = defaultdict(int)
        l = r = 0

        while r < len(s):
            window[s[r]] += 1

            if s[r] in target and target[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l,r]
                    
                

                window[s[l]] -= 1

                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                
                l += 1

            r += 1
        
        newL, newR = res
        return s[newL:newR+1] if resLen != float("inf") else ""
    