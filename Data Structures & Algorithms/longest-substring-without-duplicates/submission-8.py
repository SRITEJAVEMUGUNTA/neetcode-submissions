
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        mySet = set()
        while r < len(s):
            while s[r] in mySet:
                mySet.remove(s[l])
                l+=1
            mySet.add(s[r])
            res = max(res, r-l+1)

            r+=1
        
        return res
