from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = Counter(s)
        dicT = Counter(t)\


        for key in dicS:
            if dicS[key] != dicT[key]:
                return False

        for key in dicT:
            if dicS[key] != dicT[key]:
                return False

        return True
        

