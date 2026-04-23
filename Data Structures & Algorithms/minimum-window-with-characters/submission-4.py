class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
    
        target = Counter(t)

      

        window = {}

        res, resLen = [-1, -1], float("inf")

        have, need = 0, len(target)

        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
                
            while(have == need):
                if(resLen > r - l + 1):
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1

                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
            
        return s[l:r+1] if resLen != float("inf") else ""

