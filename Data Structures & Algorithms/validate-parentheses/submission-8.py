class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brack = {")": "(", "]": "[", "}": "{"}

        for x in s:
            if x in brack:
                if stack and brack[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
            
        return True if not stack else False