from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            dic["".join(sorted(list(string)))].append(string)
        
        return list(dic.values())