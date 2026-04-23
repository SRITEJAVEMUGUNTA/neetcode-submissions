class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []


        for val in tokens:

            
            if val == "+":
                two = stack.pop()
                one = stack.pop()
                stack.append(one + two)
            elif val == "-":
                two = stack.pop()
                one = stack.pop()
                stack.append(one - two)
            elif val == "*":
                two = stack.pop()
                one = stack.pop()
                stack.append(one * two)
            elif val == "/":
                two = stack.pop()
                one = stack.pop()
                stack.append(int(float(one) / two))
            else:
                stack.append(int(val))

        return stack[0]

