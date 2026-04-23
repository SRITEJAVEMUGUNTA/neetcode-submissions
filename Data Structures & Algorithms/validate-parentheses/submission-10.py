class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in dic:
                if stack and stack[-1] == dic[char]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

