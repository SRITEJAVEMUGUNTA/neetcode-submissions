class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = Counter(s)
        dic2 = Counter(t)

        mySet = set(s + t)

        for x in mySet:
            if x not in dic1:
                dic1[x] = 0
            if x not in dic2:
                dic2[x] = 0
            if x in dic1 and dic2:
                if(dic1[x] != dic2[x]):
                    return False
        return True