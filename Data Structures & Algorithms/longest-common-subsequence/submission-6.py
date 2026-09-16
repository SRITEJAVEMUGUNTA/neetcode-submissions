class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        dic = {}
        def memo(idxOne, idxTwo):
            if idxOne == len(text1) or idxTwo == len(text2):
                return 0
            
            if (idxOne,idxTwo) in dic: return dic[(idxOne,idxTwo)]

            val = 0

            if text1[idxOne] == text2[idxTwo]:
                val = memo(idxOne+1, idxTwo+1) + 1
            else:
                val = max(memo(idxOne+1, idxTwo), memo(idxOne,idxTwo+1))

            dic[(idxOne,idxTwo)] = val
            return val
            

        return memo(0,0)

            
