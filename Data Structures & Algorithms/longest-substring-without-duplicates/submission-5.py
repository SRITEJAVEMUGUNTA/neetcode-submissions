class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = 0
        l = 0
        letSet = set()

        for r in range(len(s)):
            while(s[r] in letSet):
                letSet.remove(s[l])
                l += 1
            letSet.add(s[r])
            sol = max(sol, r-l+1)
        
        return sol
