class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def helper(string, idx):
            if idx == len(digits):
                res.append(string)
                return
            
            combo = dic[digits[idx]]
            for char in combo:
                helper(string + char, idx+1)
            

        
        helper("", 0)
        return res


