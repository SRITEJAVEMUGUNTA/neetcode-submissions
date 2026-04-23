class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        def helper(idx):
            if idx == len(s): return True

            if idx in dic: return dic[idx]
            

            flag = False
            for word in wordDict:
                L = len(word)
                if s[idx: idx+L] == word and helper(idx+L):
                    flag = True
                    break

            if not flag:
                dic[idx] = False
                return False
            dic[idx] = True
            return True

        return helper(0)