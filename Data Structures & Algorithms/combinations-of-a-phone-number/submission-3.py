class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(idx, string):
            if idx == len(digits):
                if string:
                    res.append(string)
                return
            
            for letter in dic[digits[idx]]:
                backtrack(idx + 1, string + letter)
        
        backtrack(0, "")
        return res