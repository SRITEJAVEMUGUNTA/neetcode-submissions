class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxOcc = 0
        dic = defaultdict(int)
        length = 0
        l = 0
        for r, char in enumerate(s):
            dic[char] += 1

            maxOcc = max(dic[char], maxOcc)

            if r-l+1  - maxOcc > k:
                charToRemove = s[l]
                dic[charToRemove] -= 1
                l += 1

            length = max(length, r-l+1)

        return length