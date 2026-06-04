class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        best = 0
        for r in range(len(s)):
            let = s[r]

            while let in mySet:
                word_to_remove = s[l]
                mySet.remove(word_to_remove)
                l += 1
            
            mySet.add(let)
            best = max(best, r-l+1)

        return best
