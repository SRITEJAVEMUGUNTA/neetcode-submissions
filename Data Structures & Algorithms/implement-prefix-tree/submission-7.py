class Node:
    def __init__(self, val="", children = {}, end=False):
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                newNode = Node()
                node.children[char] = newNode
                
            node = node.children[char]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]

        return node.end

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]

        return True