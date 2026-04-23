class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.prev = self.tail
        self.tail.next = self.head
        self.capacity = capacity
        self.dic = {} # Key to node

    def remove(self, node: Node) -> None:
        prev = node.prev
        nextNode = node.next
        nextNode.prev = prev
        prev.next = nextNode

    def add(self, node:Node) -> None:
        prev = self.head.prev
        self.head.prev = node
        node.prev = prev
        prev.next = node
        node.next = self.head

    def get(self, key: int) -> int:
        
        if key not in self.dic:
            return -1
        node = self.dic[key]
        val = node.val

        self.remove(node)
        self.add(node)
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            del self.dic[key]

        newNode = Node(key, value)

        self.dic[key] = newNode

        self.add(newNode)

        if len(self.dic) > self.capacity:
            nodeToRemove = self.tail.next
            del self.dic[nodeToRemove.key]
            self.remove(nodeToRemove)


        
