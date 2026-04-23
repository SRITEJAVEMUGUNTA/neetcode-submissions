from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        biggestOccurence = 0
        res = 0
        dic = defaultdict(int)

        while r < len(s):
            char = s[r]
            dic[char] += 1

            biggestOccurence = max(biggestOccurence, dic[char])

            while (r-l+1) - biggestOccurence > k:
                charToRemove = s[l]
                dic[charToRemove] -= 1
                l += 1

            res = max(res,r-l+1)
            r += 1

        return res