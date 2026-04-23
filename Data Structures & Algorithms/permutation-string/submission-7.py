class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0 for _ in range(26)]
        arr2 = [0 for _ in range(26)]

        if len(s1) > len(s2): return False

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if arr1[i] == arr2[i]:
                count += 1

        l = 0
        print(count)
        for i in range(len(s1), len(s2)):
            if count == 26:
                return True
            idx = ord(s2[i]) - ord('a')
            arr2[idx] += 1

            if arr2[idx] == arr1[idx]: count += 1
            if arr2[idx] - 1 ==  arr1[idx]: count -= 1
            

            idxToRemove = ord(s2[l]) - ord('a')

            arr2[idxToRemove] -= 1

            if arr2[idxToRemove] == arr1[idxToRemove]: count += 1
            if arr2[idxToRemove] + 1 ==  arr1[idxToRemove]: count -= 1
            l += 1
        
        print(count)
        return count == 26

