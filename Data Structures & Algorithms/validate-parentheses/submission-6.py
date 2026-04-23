class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brack = {")": "(", "]": "[", "}": "{"}

        for x in s:
            if x in brack:
                if(stack and brack[x] == stack[-1]):
                    stack.pop()
                    continue

                else:
                    return False
        
            stack.append(x)
        return True if not stack else False