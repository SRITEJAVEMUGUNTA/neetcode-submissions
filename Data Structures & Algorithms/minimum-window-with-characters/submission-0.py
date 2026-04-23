class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count, wind = {}, {}

        for x in t:
            count[x] = 1 + count.get(x,0)

        have, need = 0, len(count)
        

        l = 0

        res, resLen = [-1,-1], float("inf")

        for r in range(len(s)):
            c = s[r]

            wind[c] = 1 + wind.get(c,0)

            if(c in t and wind[c] == count[c]):
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                

                wind[s[l]] -= 1

                if(s[l] in t and wind[s[l]] < count[s[l]]):
                    have -=1
                
                l += 1
        
        l, r = res

        if(resLen != float("inf")):
            return(s[l:r+1])
        else:
            return ""

