class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [[0 for _ in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        lastRow = [0 for _ in range(len(text2)+1)]
        for r in range(len(text1)-1,-1,-1):
            arr = [0 for _ in range(len(text2)+1)]
            for c in range(len(text2)-1,-1,-1):
                if text1[r] == text2[c]:
                    arr[c] = 1 + lastRow[c+1]
                else:
                    arr[c] = max(arr[c+1], lastRow[c])
            lastRow = arr
        return lastRow[0]