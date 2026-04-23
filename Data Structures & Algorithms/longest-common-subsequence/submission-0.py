class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dic = {}

        def helper(one, two):
            if one >= len(text1) or two >= len(text2):
                return 0

            if (one,two) in dic:
                return dic[(one,two)]
            if text1[one] == text2[two]:
                return 1 + helper(one+1, two+1)
            
            num =  max(helper(one+1,two), helper(one, two+1))
            dic[(one,two)] = num
            return num
        

        return helper(0,0)