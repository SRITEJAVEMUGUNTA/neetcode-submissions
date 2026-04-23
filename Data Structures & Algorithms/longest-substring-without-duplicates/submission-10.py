class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()


        l, r = 0,0
        res = 0
        while r < len(s):
            char = s[r]

            while char in mySet:
                charToRemove = s[l]
                mySet.remove(charToRemove)
                l += 1
            
            mySet.add(char)
            res = max(res, r-l+1)
            r += 1

        return res