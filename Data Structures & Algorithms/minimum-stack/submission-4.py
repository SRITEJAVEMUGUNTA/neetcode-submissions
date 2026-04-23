class Node:
    def __init__(self, val=0, nxt=None, small=0):
        self.val = val
        self.nxt = nxt
        self.smallest = small
class MinStack:
    def __init__(self):
        self.head = Node()
        self.cur = self.head
        self.smallest = float("inf")
    def push(self, val: int) -> None:
        newNode = Node(val)
        if self.smallest > val:
            self.smallest = val
        newNode.smallest = self.smallest
        newNode.nxt = self.head.nxt
        self.head.nxt = newNode
    def pop(self) -> None:
        self.head.nxt = self.head.nxt.nxt
        self.smallest = self.head.nxt.smallest if self.head.nxt else float("inf")
    def top(self) -> int:
        print(self.head.val)
        return self.head.nxt.val

    def getMin(self) -> int:
        return self.head.nxt.smallest