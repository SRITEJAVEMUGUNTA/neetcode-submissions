class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = [0]
        resIdx = [0]
        def helper(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen[0]:
                    resLen[0] = (r-l+1)
                    resIdx[0] = l
                l -= 1
                r += 1
        

        for i in range(len(s)):
            helper(i,i)
            helper(i, i+1)
        
        return s[resIdx[0] : resIdx[0] + resLen[0]]
        