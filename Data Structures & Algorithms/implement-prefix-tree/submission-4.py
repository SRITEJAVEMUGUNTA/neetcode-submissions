class Node:
    def __init__(self, val="", children=None, isEnd = False):
        self.val = val
        self.children = children if children is not None else {}
        self.isEnd = isEnd
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        i = 0

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        i = 0
        node = self.root
        while node and i < len(word):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False

            i += 1

        return True if node.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        i = 0
        node = self.root
        while node and i < len(prefix):
            if prefix[i] in node.children:
                node = node.children[prefix[i]]
            else:
                return False

            i += 1
        

        return True
        