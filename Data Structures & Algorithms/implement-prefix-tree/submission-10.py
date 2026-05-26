class Node:
    def __init__(self):
        self.dic = {} # letter to node
        self.letter = ""
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for let in word:
            if let not in node.dic:
                newNode = Node()
                newNode.letter = let
                node.dic[let] = newNode

            node = node.dic[let]

        
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for let in word:
            if let not in node.dic:
                return False
            else:
                node = node.dic[let]

            
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for let in prefix:
            if let not in node.dic:
                return False
            else:
                node = node.dic[let]

            
        return True
        