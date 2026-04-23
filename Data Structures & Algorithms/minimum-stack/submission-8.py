class Node:
    def __init__(self, next = None, val=0, small = float("Inf")):
        self.next = next
        self.small = small
class MinStack:
    def __init__(self):
        self.head = None
        self.smallest = float("inf")
    def push(self, val: int) -> None:
        newNode = Node()
        newNode.val = val
        self.smallest = min(self.smallest, val)
        newNode.small = self.smallest
        print(self.smallest)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode


    def pop(self) -> None:
        if not self.head: return -1
        node = self.head
        self.head = self.head.next
        self.smallest = self.head.small if self.head else float("inf")
        return node.val



    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.small
