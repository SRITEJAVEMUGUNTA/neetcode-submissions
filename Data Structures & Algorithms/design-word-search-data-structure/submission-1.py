class Node:
    def __init__(self, val="", children=None, isEnd = False):
        self.val = val
        self.children = children if children is not None else {}
        self.isEnd = isEnd


class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]

        node.isEnd = True
    


        
    def search(self, word: str) -> bool:
        

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                
                if word[i] == ".":
                    for node in cur.children.values():
                        if dfs(i+1, node):
                            return True
                    return False
                elif word[i] not in cur.children:
                    return False
                
                cur = cur.children[word[i]]

            return cur.isEnd
        
        return dfs(0, self.root)
            

