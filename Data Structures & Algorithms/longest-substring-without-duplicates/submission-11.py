class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res = 0
        for r in range(len(s)):
            char = s[r]

            while char in seen:
                charToRemove = s[l]
                seen.remove(charToRemove)
                l += 1

            seen.add(char)
            
            res = max(res, r-l+1)

        return res