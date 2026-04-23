class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr1 = [0 for i in range(26)]
        arr2 = [0 for i in range(26)]

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord("a")] += 1
            arr2[ord(s2[i]) - ord("a")] += 1

        
        count = 0

        for num in range(26):
            if arr1[num] == arr2[num]:
                count += 1

        l = 0

        for i in range(len(s1), len(s2)):
            if count == 26:
                return True
            
            print(arr2)

            idx = ord(s2[i]) - ord("a")
            arr2[idx] += 1
            if arr2[idx] == arr1[idx]:
                count += 1
            elif arr2[idx] - 1 == arr1[idx]:
                count -= 1
            

            removedIdx = ord(s2[l]) - ord("a")

            arr2[removedIdx] -= 1
            if arr2[removedIdx] == arr1[removedIdx]:
                count += 1
            elif arr2[removedIdx] + 1 == arr1[removedIdx]:
                count -= 1

            l += 1

        return count == 26

            
