class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set()
        ops.add('+')
        ops.add('-')
        ops.add('*')
        ops.add('/')
        for item in tokens:
            if item in ops:
                two = stack.pop()
                one = stack.pop()

                if item == "+":
                    stack.append(one + two)
                elif item == "-":
                    stack.append(one - two)
                elif item == "*":
                    stack.append(one * two)
                else:
                    stack.append(int(float(one)/two))
            else:
                stack.append(int(item))

        return stack[-1]
