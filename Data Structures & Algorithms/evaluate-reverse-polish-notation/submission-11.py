class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # -220 17
        for op in tokens:
            if op == "+":
                two = stack.pop()
                one = stack.pop()
                stack.append(one+two)
            elif op == "-":
                two = stack.pop()
                one = stack.pop()
                stack.append(one-two)
            elif op == "*":
                two = stack.pop()
                one = stack.pop()
                stack.append(one*two)
            elif op == "/":
                two = stack.pop()
                one = stack.pop()
                stack.append(int(one / two))
            else:
                stack.append(int(op))

        

        return stack[-1]