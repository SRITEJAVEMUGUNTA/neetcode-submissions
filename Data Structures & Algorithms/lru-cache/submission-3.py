class ListNode:
    def __init__(self,val=0, key=0):
        self.key=key
        self.val= val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.dic = {}
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
    def add(self, node: ListNode) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.next,nxt.prev = node, node
        node.next, node.prev = nxt, prev
    def remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev
        node.next = node.prev = None

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        
        self.dic[key] = ListNode(value,key)
        self.add(self.dic[key])

        if len(self.dic) > self.capacity:
            lru = self.head.next
            key = lru.key
            self.remove(lru)
            del self.dic[key]
        