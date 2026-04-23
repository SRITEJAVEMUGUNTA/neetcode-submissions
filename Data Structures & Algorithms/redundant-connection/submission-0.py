from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        
        visiting = set()
        def dfsCycleCheck(prev, node):
            if node in visiting:
                
                return False

            visiting.add(node)

            for nei in dic[node]:
                if prev == nei:
                    continue
                
                if not dfsCycleCheck(node, nei):
                    return False
                
            visiting.remove(node)

            return True






        for nodeOne, nodeTwo in edges:
            dic[nodeOne].append(nodeTwo)
            dic[nodeTwo].append(nodeOne)

            if not dfsCycleCheck(None, nodeOne):

                return [nodeOne, nodeTwo]

            