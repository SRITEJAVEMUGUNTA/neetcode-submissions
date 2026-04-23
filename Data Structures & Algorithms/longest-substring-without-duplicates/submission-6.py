class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0

        best = 0

        for r in range(len(s)):
            while(s[r] in mySet):
                mySet.remove(s[l])
                l+=1
            mySet.add(s[r])
            best = max(best, len(mySet))
        
        return best
