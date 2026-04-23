from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)

        res = float("-inf")
        l, r = 0,0
        maxOcc = float("-inf")
        while r < len(s):
            char = s[r]
            dic[char] += 1
            maxOcc = max(maxOcc,dic[char])

            if (r-l+1) - maxOcc <= k:
                res = max(res, r-l+1)
            else:
                charToRemove = s[l]
                dic[charToRemove] -= 1
                l += 1

            r += 1

        return res