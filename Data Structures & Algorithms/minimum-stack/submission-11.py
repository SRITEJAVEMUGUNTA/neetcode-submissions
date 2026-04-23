class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_element = float("inf")

    def push(self, val: int) -> None:
        self.min_element = min(self.min_element, val)
        self.stack.append(val)
        self.min_stack.append(self.min_element)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.min_element = self.min_stack[-1]
        else:
            self.min_element = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
