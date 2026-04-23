class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char not in dic:
                stack.append(char)
            else:
                if not stack: return False

                if not stack[-1] == dic[char]: return False
                stack.pop()

        return len(stack) == 0