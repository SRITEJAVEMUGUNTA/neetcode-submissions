class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}

        def helper(idx):
            if idx == len(s):
                return True
            
            if idx in dic:
                return dic[idx]
            
            flag = False
            for word in wordDict:
                lenWord = len(word)
                if word == s[idx:idx+lenWord] and helper(idx+lenWord):
                    flag = True
                    break
            dic[idx] = flag
            return flag

        return helper(0)
