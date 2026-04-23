class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for x in s:
            if x.isalnum():
                res += x.lower()
            else:
                continue
        print(res)

        return res == res[::-1]