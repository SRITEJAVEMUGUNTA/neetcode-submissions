class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        order = {")": "(", "]": "[", "}": "{"}

        for x in s:
            if x in order:
                if(stack and order[x] == stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False