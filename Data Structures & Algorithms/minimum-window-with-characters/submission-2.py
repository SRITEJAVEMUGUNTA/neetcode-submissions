class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        target = Counter(t)

        window = {}

        res = [-1,-1]
        resLen = float("inf")

        l = 0

        have, need = 0, len(target)

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in target and window[c] == target[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                q = s[l]

                window[q] -= 1

                if(q in target and window[q] < target[q]):
                    have -= 1
                l+=1

        l, r = res
        
        if(resLen != float("inf")):
            return s[l:r+1]
        else:
            return ""