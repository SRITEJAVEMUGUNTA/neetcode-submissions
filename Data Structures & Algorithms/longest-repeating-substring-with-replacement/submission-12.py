from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = defaultdict(int) # letter: count
        maxCount = 0
        length = 0
        for r in range(len(s)):
            curLetter = s[r]
            dic[curLetter] += 1
            if dic[curLetter] > maxCount:
                maxCount = dic[curLetter]
            
            
            if (maxCount + k) < (r-l+1):
                letter_to_remove = s[l]
                dic[letter_to_remove]-=1
                l+=1

            
            length = max(length, r-l+1)

        
        return length
