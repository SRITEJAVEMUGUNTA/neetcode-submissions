class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        backward = []


        for x in s:
            if x.isalnum():
                forward.append(x.lower()) 


        for x in range(len(s)-1, -1, -1):
            if s[x].isalnum():
                backward.append(s[x].lower())  

       
        return forward == backward